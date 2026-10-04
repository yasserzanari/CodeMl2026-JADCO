# JADCO — notebook d’analyse

## Livrable principal

`jadco-final.ipynb` est l’unique notebook du dépôt et le livrable principal de l’analyse. Il est adapté du notebook de départ `starter.ipynb` et contient les étapes de préparation, les hypothèses, les fonctions `estimate_2026()` et `backtest()`, ainsi que les références méthodologiques.

`jadco_analysis.py` est un module auxiliaire réutilisable; ce n’est pas un second livrable Jupyter.

## Exécution

Python 3.10 ou ultérieur avec les dépendances de `requirements.txt`. Ouvrez `jadco-final.ipynb` dans Jupyter et exécutez les cellules dans l’ordre. Les quatre CSV autorisés doivent être fournis localement dans `entrees-locales/` ou via la variable `JADCO_INPUT_DIR`. Aucune donnée CRM du défi n’est incluse dans ce dépôt. Les sources publiques requises par les sections correspondantes doivent également être disponibles sous `externes/`.

Les sorties, graphiques et exports créés pendant l’exécution peuvent révéler des résultats dérivés des données privées. Gardez-les dans l’environnement autorisé et effacez les sorties avant de committer le notebook. Cette branche ne publie ni les résultats empiriques ni les fichiers CRM.

## Portée

Le notebook contient le code d’estimation et de backtest, mais n’est pas livré avec les résultats calculés sur les données privées. Aucun modèle entraîné n’est utilisé. La présentation du jury n’est pas incluse dans cette branche.

Les sources publiques, règles réglementaires et outil d’IA utilisé sont référencés à la fin du notebook.
