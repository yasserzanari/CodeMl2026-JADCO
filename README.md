# JADCO — The Optimizers

**CodeML 2026 · JADCO – Clés en main · Collection Équinoxe**

> **English summary:** This repository publishes the JADCO analysis notebook, methodology, and public reference data. Challenge CRM records and data-derived outputs are excluded.

## Question et mesure choisie

Le notebook estime la médiane de la variation annualisée du **loyer effectif** (`sRentEffective`) entre deux baux consécutifs de la même unité, pour les baux qui commencent pendant l’année visée. L’appariement utilise `sPropCode` + `sUnitCode`; chaque transition admissible reçoit le même poids.

Cette cible mesure une variation entre transitions comparables. Elle ne mesure ni la croissance des revenus du portefeuille, ni un indice de marché, ni la hausse à appliquer à un bail individuel. Le loyer effectif est privilégié parce que le champ fourni tient compte des concessions. Le notebook le compare au loyer contractuel et audite l’attribution des crédits sans appliquer une seconde déduction non documentée.

## Ce que le travail couvre

Le notebook [jadco-final.ipynb](jadco-final.ipynb), adapté du notebook de départ officiel, contient le code d’analyse et les contrôles demandés :

1. **Définir la question :** préciser la cible, la population, les exclusions et la pondération.
2. **Analyser les colonnes :** contrôler les types, dates, valeurs manquantes, doublons et clés avant transformation; examiner comment la composition influe sur les médianes annuelles.
3. **Comparer à unité constante :** apparier les baux consécutifs d’une même unité, exclure les écarts non comparables et annualiser la variation.
4. **Traiter les concessions :** comparer les loyers contractuels et effectifs et documenter les limites de rattachement aux baux.
5. **Séparer les segments :** analyser renouvellements et relocations séparément; utiliser les références de l’Ontario pour Ottawa et ne pas transposer les règles du Québec.
6. **Ajouter le contexte public :** comparer les séries SCHL et IPC aux tendances internes sans confondre leurs populations ou définitions; citer le TAL et les sources ontariennes pour le contexte réglementaire.
7. **Prévoir et valider :** compléter `estimate_2026(leases, asking, external=None)` et `backtest(leases, target_year)`, avec coupures temporelles, méthodes comparées, hypothèses et diagnostics historiques.

Les cellules de code et les visualisations reproductibles sont conservées. Cette copie GitHub ne contient pas les sorties exécutées ni les commentaires narratifs chiffrés. Les années examinées pendant le développement sont qualifiées d’exploratoires, pas de validation indépendante.

## Exécuter le notebook sans écrire de résultats dans ce dépôt

Les quatre CSV du défi doivent être obtenus par un canal autorisé et gardés hors du dépôt. Créer un espace local distinct, y copier le notebook, `requirements.txt` et le dossier `externes/`, puis exécuter le tout depuis cet espace :

```powershell
$localWork = 'C:\jadco-local'
New-Item -ItemType Directory -Force "$localWork\externes" | Out-Null
Copy-Item jadco-final.ipynb, requirements.txt $localWork
Copy-Item externes\* "$localWork\externes"
$env:JADCO_INPUT_DIR = 'C:\chemin\vers\les\quatre-csv-autorises'
Set-Location $localWork
python -m pip install -r requirements.txt
python -m jupyter nbconvert --execute --to notebook --inplace jadco-final.ipynb
```

On peut aussi définir `JADCO_PACKAGE_PATH` vers l’archive locale officielle au lieu de `JADCO_INPUT_DIR`. Le notebook vérifie le manifeste de l’archive avant de lire les fichiers. Il ne télécharge et ne transmet aucune donnée CRM. L’exécution produit des sorties dans l’espace local de travail; ne pas les recopier dans ce dépôt public.

`requirements.txt` consigne les versions utilisées. L’environnement de référence est Python 3.11 avec pandas, NumPy, Matplotlib, Jupyter et IPython.

## Sources et reproductibilité

Le dossier `externes/` ne contient que des tableaux et extraits publics de la SCHL et de Statistique Canada, accompagnés des métadonnées de source. Aucun CSV CRM n’est inclus. Les produits, liens officiels, attributions, licences, références TAL/Ontario et outils d’IA figurent dans [SOURCES.md](SOURCES.md).

La SCHL permet la redistribution de ses informations sous réserve de ses conditions et avis de source. Les données de Statistique Canada sont fournies sous sa Licence ouverte. Ces organismes n’endossent pas ce projet. Lire et accepter les modalités de chaque source avant de réutiliser ses fichiers.

## Portée et limites

Les résultats dépendent des données de défi autorisées et des hypothèses documentées. Les champs fournis ne confirment pas toutes les conventions de crédits, les dates de saisie ou de révision, ni chaque situation réglementaire individuelle. Le notebook expose ces limites et utilise des analyses de sensibilité lorsqu’elles sont possibles. Le résultat est une analyse statistique, pas un avis juridique ni une recommandation de loyer individuel.

Les estimations confidentielles, graphiques et diapositives qui présentent des résultats issus du CRM sont exclus de GitHub. Le code, la méthode et les sources publiques sont publiés ici; les pièces avec résultats sont réservées au canal autorisé des juges.
