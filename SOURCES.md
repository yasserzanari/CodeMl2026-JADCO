# Sources, licences et assistance IA

Ce dépôt cite les sources publiques utilisées pour le contexte de marché et le cadre réglementaire. Les extraits publics de `externes/` ne contiennent pas les données du défi. La date de référence et les transformations figurent dans le notebook et dans les métadonnées accompagnant chaque source.

## Sources publiques de marché

| Organisme et produit | Usage dans le projet | Référence |
|---|---|---|
| Société canadienne d’hypothèques et de logement (SCHL), *Rental Market Survey Data Tables*, éditions Ontario et Québec | Contexte locatif et comparaison avec la mesure interne | [Tableaux de l’Enquête sur les logements locatifs](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables/rental-market/rental-market-report-data-tables) |
| SCHL, éditions historiques des tableaux de l’Enquête sur les logements locatifs | Comparaisons historiques en respectant les dates de publication et les révisions de séries | [Tableaux de l’Enquête sur les logements locatifs](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables/rental-market/rental-market-report-data-tables) |
| SCHL, *Housing Supply Report*, Fall 2025 | Contexte descriptif de l’offre en construction | [Rapport sur l’offre de logements (PDF)](https://assets.cmhc-schl.gc.ca/sites/cmhc/professional/housing-markets-data-and-research/market-reports/housing-supply-report/2025/housing-supply-report-2025-fall-en.pdf?rev=e2bdcf1d-e5d4-4310-a80c-b543872dcbbb) |
| Statistique Canada, tableau 18-10-0004-01, Indice des prix à la consommation, loyers | Comparateur externe; ses dates de diffusion sont prises en compte dans les coupures | [Téléchargement du tableau](https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/18100004/en) |
| Statistique Canada et SCHL, tableau 34-10-0134-01, mises en chantier, logements en construction et achèvements | Référence contextuelle documentée; ne constitue pas une variable CRM | [Tableau 34-10-0134-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410013401) |
| Statistique Canada, tableau 34-10-0292-01, permis de bâtir | Source examinée et écartée comme prédicteur dans cette analyse | [Tableau 34-10-0292-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3410029201) |

### Avis et licences

Pour les extraits de données SCHL redistribués ici, l’avis de source est :

> Source: Canada Mortgage and Housing Corporation (CMHC), Rental Market Survey Data Tables and Housing Supply Report, reference periods identified in the accompanying source metadata. This information is reproduced and distributed on an “as is” basis with the permission of CMHC.

Les destinataires des données SCHL doivent accepter [l’entente de licence SCHL](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/cmhc-licence-agreement-use-of-data). La SCHL conserve ses droits et n’endosse pas ce projet. Les périodes exactes sont indiquées dans les fichiers de provenance.

Pour Statistique Canada :

> Adapted from Statistics Canada, Consumer Price Index, table 18-10-0004-01, reference periods identified in the accompanying source metadata. This does not constitute an endorsement by Statistics Canada of this product.

Voir la [Licence ouverte de Statistique Canada](https://www.statcan.gc.ca/en/terms-conditions/open-licence). Les données sont reproduites fidèlement; les sources et périodes sont indiquées et aucune affiliation ou approbation n’est revendiquée.

## Références réglementaires

Ces liens sont des sources officielles de référence, pas une détermination de la loi applicable à un logement particulier. Le notebook traite Ottawa selon les références ontariennes et consulte séparément les ressources du Tribunal administratif du logement pour le Québec.

- Ontario, [Residential rent increases](https://www.ontario.ca/page/residential-rent-increases).
- Ontario, [Guide to the standard lease for rental housing](https://files.ontario.ca/mmah-guide-to-standard-lease-for-rental-housing-en-2022-04-19.pdf).
- Tribunals Ontario, [A guide to the Residential Tenancies Act](https://tribunalsontario.ca/documents/ltb/Brochures/A%20Guide%20to%20the%20Residential%20Tenancies%20Act.html).
- Tribunal administratif du logement (Québec), [Fixation de loyer et reconduction du bail](https://www.tal.gouv.qc.ca/fr/reconduction-du-bail-et-fixation-de-loyer/augmentation-de-loyer) et [modification d’une condition du bail](https://www.tal.gouv.qc.ca/fr/reconduction-du-bail-et-fixation-de-loyer/modification-d-une-condition-du-bail).

## Outil d’IA

**OpenAI Codex** a assisté le développement et la révision du code ainsi que la rédaction de documentation. L’équipe demeure responsable des définitions, des choix de méthode, de la validation et de toute présentation des résultats. Aucune donnée CRM n’est jointe à cette documentation publique.
