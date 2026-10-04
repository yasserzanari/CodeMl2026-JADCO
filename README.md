# JADCO — code d’analyse

Ce dépôt contient une version partageable du code méthodologique JADCO. Le notebook [jadco_analysis.ipynb](jadco_analysis.ipynb) et le module [jadco_analysis.py](jadco_analysis.py) fournissent les fonctions d’appariement à unité constante, d’estimation 2026 et de backtest.

## Portée de cette version

Le notebook contient le code source sans données d’entrée ni sorties exécutées. Il ne s’agit pas du notebook de résultats complet remis au jury. Les CSV CRM, les graphiques, les tableaux et les résultats dérivés restent dans l’environnement privé autorisé et ne sont pas inclus dans cette branche.

## Exécution locale

Python 3.10 ou ultérieur avec les dépendances de `requirements.txt`. Chargez les tables autorisées dans votre environnement privé, puis fournissez-les aux interfaces `estimate_2026(leases, asking, external=None)` et `backtest(leases, asking, target_year, external=None)`. Le code ne charge ni n’enregistre de fichiers. Gardez les entrées et résultats hors du dépôt.

## Méthode

Les transitions sont appariées par `sPropCode` + `sUnitCode`. Le code calcule séparément les variations contractuelles et effectives; le moteur construit la prévision à partir de l’historique disponible à la coupure et compare la prévision à l’observation dans une étape distincte. Les hypothèses de disponibilité des données et les limites du backtest doivent être considérées lors de l’interprétation.

Le code est dérivé du notebook de travail JADCO. Les sources publiques utilisées par l’analyse complète sont documentées dans la remise privée.
