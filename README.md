# JADCO — code d’analyse

Ce dépôt contient le code méthodologique du projet JADCO, extrait et adapté du notebook de travail. Les fonctions d’appariement à unité constante, d’estimation 2026 et de backtest sont fournies sans données d’entrée, sorties de notebook, graphiques ni résultats empiriques.

## Confidentialité et utilisation

Les fichiers CRM et toutes les données fournies par le défi doivent rester dans un emplacement local autorisé. Ce dépôt ne contient aucun fichier de données. N’y ajoutez pas de sorties calculées, tableaux, graphiques, captures ou présentations dérivés de ces données. Le module renvoie les résultats à l’appelant : gardez-les dans l’environnement privé du projet.

## Méthode dans le code

`jadco_analysis.py` apparie les baux consécutifs par `sPropCode` + `sUnitCode`, filtre les écarts de durée configurés, calcule les croissances contractuelles et effectives, construit une prévision à partir des baux connus à la date de coupure et compare séparément cette prévision à la cible observée. `estimate_2026()` et `backtest()` sont des interfaces réutilisables; elles ne chargent ni n’écrivent de fichiers.

La méthode et ses paramètres sont explicités dans le code. Le résultat d’un backtest dépend de la définition de disponibilité des champs historiques, des données fournies à l’appel et de la configuration choisie. Une exécution sans les données CRM autorisées n’est pas incluse dans ce dépôt.

## Environnement

Python 3.10 ou ultérieur avec `pandas` et `numpy`. Les données `asking` et `external` sont fournies séparément par l’appelant avec les colonnes requises par le moteur. Ne placez pas les entrées ou résultats dans ce dépôt.

## Références

Le code est dérivé du notebook de travail JADCO et des consignes du défi. Les sources publiques utilisées par l’analyse complète sont documentées dans l’espace privé de remise; aucune série dérivée n’est republiée ici.
