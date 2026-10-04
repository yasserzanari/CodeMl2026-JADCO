"""JADCO analysis methods, extracted from the project notebook.

This module contains code only. Do not place CRM inputs or derived outputs in this repository.
"""
from dataclasses import dataclass
import numpy as np
import pandas as pd

UNIT_KEY = ["sPropCode", "sUnitCode"]
METHODS = ("A_derniere", "B_robuste_segmentee", "C_B_plus_IPC")
SELECTED_METHOD = "A_derniere"

@dataclass(frozen=True)
class Protocol:
    min_gap_years: float = 0.5
    max_gap_years: float = 2.5
    days_per_year: float = 365.25
    history_years: int = 3
    min_segment_pairs: int = 30
    min_output_pairs: int = 30
    cpi_anchor_weight: float = 0.5
    complexity_gain_pp: float = 0.25
    availability: str = "contractual"
    last_pair_per_unit: bool = False
    clip_quantiles: tuple = (0.0, 1.0)

CONFIG = Protocol()

def prepare_leases(frame):
    result = frame.copy()
    for col in ['sLeaseFrom', 'sLeaseTo', 'sSignDate', 'sAvailable']:
        result[col] = pd.to_datetime(result[col], errors='raise')
    result['year'] = result.sLeaseFrom.dt.year
    return result

def same_unit_pairs(frame, config=CONFIG):
    data = prepare_leases(frame).sort_values(UNIT_KEY + ['sLeaseFrom']).copy()
    for col in ['sRent','sRentEffective','sLeaseFrom','sTermSeq']:
        data['prev_' + col] = data.groupby(UNIT_KEY)[col].shift()
    data['gap_years'] = (data.sLeaseFrom-data.prev_sLeaseFrom).dt.days / config.days_per_year
    valid = data.gap_years.between(config.min_gap_years,config.max_gap_years,inclusive='neither')
    for col in ['sRent','sRentEffective']:
        valid &= data[col].gt(0) & data['prev_'+col].gt(0)
    exclusions = {'premiers_baux': int(data.prev_sLeaseFrom.isna().sum()),
                  'ecarts_courts': int(data.gap_years.le(config.min_gap_years).sum()),
                  'ecarts_longs': int(data.gap_years.ge(config.max_gap_years).sum()),
                  'paires_valides': int(valid.sum())}
    pairs = data.loc[valid].copy()
    pairs['contract_growth'] = ((pairs.sRent / pairs.prev_sRent)**(1/pairs.gap_years)-1)*100
    pairs['effective_growth'] = ((pairs.sRentEffective / pairs.prev_sRentEffective)**(1/pairs.gap_years)-1)*100
    if config.last_pair_per_unit:
        pairs = pairs.drop_duplicates(UNIT_KEY + ['year'],keep='last')
    return pairs, exclusions

def history_at(frame, cutoff, config):
    data=prepare_leases(frame)
    known=data[data.sSignDate.le(cutoff)&data.sLeaseFrom.le(cutoff)].copy()
    if config.availability=='conservative':
        known=known[known.sLeaseTo.le(cutoff)].copy()
    return known

def historical_location(history, state, renewal, config, price_col):
    recent=history[history.year.ge(int(history.year.max())-config.history_years+1)]
    scopes=[recent[recent.sState.eq(state)&recent.sRenewal.eq(renewal)],
            recent[recent.sRenewal.eq(renewal)], recent]
    labels=['province_type','type','global']
    for scope,label in zip(scopes,labels):
        annual_medians=scope.groupby('year')[price_col].median()
        if (len(scope)>=config.min_segment_pairs and len(annual_medians)>=2) or label=='global':
            if annual_medians.empty: raise ValueError('Historique comparable insuffisant')
            return float(annual_medians.median()),label
    raise ValueError('Historique comparable insuffisant')

def forecast_engine(frame, asking_frame, external_frame, year, method='A_derniere',config=CONFIG,
                    price_col='effective_growth'):
    cutoff=pd.Timestamp(year=year-1,month=12,day=31)
    known=history_at(frame,cutoff,config)
    hist,_=same_unit_pairs(known,config)
    if hist.empty:raise ValueError('Aucune paire historique éligible')
    last_year=int(hist.year.max())
    reference=hist[hist.year.eq(last_year)].copy()
    available_asking=asking_frame[asking_frame.month_end.le(cutoff)].copy()
    available_external=(external_frame[external_frame.release_date.le(cutoff)&external_frame.reference_date.le(cutoff)].copy()
                        if external_frame is not None else pd.DataFrame())
    predicted=reference[price_col].to_numpy().copy()
    if config.clip_quantiles!=(0.0,1.0):
        lo,hi=hist[price_col].quantile(config.clip_quantiles)
        predicted=np.clip(predicted,lo,hi)
    if method!='A_derniere':
        for (state,renewal),group in reference.groupby(['sState','sRenewal']):
            location,scope=historical_location(hist,state,renewal,config,price_col)
            indexes=reference.index.get_indexer(group.index)
            if method=='C_B_plus_IPC':
                if available_external.empty:raise ValueError('IPC publié manquant à la coupure')
                province=available_external[available_external.geography.eq(state)].sort_values('release_date')
                if province.empty:raise ValueError('IPC provincial manquant à la coupure')
                cpi=float(province.iloc[-1].value)
                location=(1-config.cpi_anchor_weight)*location+config.cpi_anchor_weight*cpi
            predicted[indexes]+=location-float(group[price_col].median())
    if method not in METHODS:raise ValueError('Méthode inconnue')
    assert known.sLeaseFrom.max()<=cutoff and known.sSignDate.max()<=cutoff
    assert available_asking.empty or available_asking.month_end.max()<=cutoff
    assert available_external.empty or available_external.release_date.max()<=cutoff
    reference['predicted_growth']=predicted
    return {'year':year,'cutoff':str(cutoff.date()),'method':method,'estimate_pct':float(np.median(predicted)),
            'history_pairs':len(hist),'reference_pairs':len(reference),'reference_units':int(reference.hUnit.nunique()),
            'reference_year':last_year,'reference_buildings':int(reference.sBuilding.nunique()),
            'eligible_asking_rows':len(available_asking),'external_rows_available':len(available_external),
            'availability':config.availability,'samples':reference}

def observed_target(frame,year,config=CONFIG,price_col='effective_growth'):
    # Calcul séparé, après la prévision. Aucun passage de cette table au moteur.
    data=prepare_leases(frame)
    observed,_=same_unit_pairs(data[data.sLeaseFrom.le(pd.Timestamp(year,12,31))],config)
    target=observed[observed.year.eq(year)]
    if target.empty:raise ValueError('Aucune observation cible')
    return {'observed_pct':float(target[price_col].median()),'observed_pairs':len(target),
            'observed_units':int(target.hUnit.nunique()),'observed_buildings':int(target.sBuilding.nunique())}

def evaluate_method(frame, asking_frame, external_frame, year, method=SELECTED_METHOD, config=CONFIG):
    forecast=forecast_engine(frame, asking_frame, external_frame, year, method, config)
    actual=observed_target(frame,year,config)
    result={k:v for k,v in forecast.items() if k!='samples'}
    result.update(actual)
    result['error_pp']=result['estimate_pct']-result['observed_pct']
    result['absolute_error_pp']=abs(result['error_pp'])
    return result

def estimate_2026(leases, asking, external=None, config=CONFIG):
    '''Retourne la médiane prévue de hausse effective annualisée 2026, en %.'''
    return forecast_engine(leases,asking,external,2026,SELECTED_METHOD,config)['estimate_pct']

def backtest(leases, asking, target_year, external=None):
    '''Interface officielle : méthode comme à fin target_year-1, puis résultat observé séparé.'''
    return evaluate_method(leases, asking, external, int(target_year), SELECTED_METHOD, CONFIG)
