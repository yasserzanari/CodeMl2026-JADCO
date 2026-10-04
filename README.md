# Notebook public — usage et périmètre

`jadco-final.ipynb` est le notebook principal du projet JADCO, dérivé de `starter.ipynb`. Il contient le code de préparation, `estimate_2026()` et `backtest()` ainsi que la méthode et ses hypothèses. Les sorties du notebook ont été effacées pour cette copie publique.

## Données et exécution

Les fichiers CRM du défi ne sont pas inclus et ne doivent pas être publiés. Pour exécuter l'analyse, placez les quatre CSV autorisés dans `entrees-locales/` ou définissez `JADCO_INPUT_DIR` vers leur emplacement local. Les sources publiques externes utilisées par le notebook doivent être disponibles dans `externes/`. Ouvrez le fichier dans Jupyter et exécutez les cellules dans l'ordre.

Les calculs et graphiques produits à l'exécution peuvent révéler des résultats dérivés des données privées. Gardez les sorties, graphiques et exports dans l'environnement autorisé; effacez les sorties avant de committer le notebook. Aucun modèle entraîné n'est utilisé dans cette version.

## Environnement

Python 3 avec les dépendances indiquées dans `requirements.txt` (`numpy`, `pandas`). Le notebook utilise aussi Matplotlib et Jupyter/IPython. Le module `jadco_analysis.py` fournit séparément des fonctions réutilisables sans chargement de fichiers.

## Références et outils

Les sources publiques et les limites réglementaires sont référencées à la fin du notebook. Assistance IA : OpenAI Codex pour le code, l'audit et la rédaction.

