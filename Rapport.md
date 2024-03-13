# Remise de Laboratoire 2

## LOG680 – Introduction à l’approche DevOps

Groupe n°2 - Équipe n°2

### Membres de l’équipe

- Alexandre Rheault
- Hugo Rhéaume-Simard
- Sunny Modha

### Hiver 2024

#### Table des matières

- Introduction 1
- Répartition du travail 1
- Implémentation de la sauvegarde des données de température dans la base de données 2
- Implémentation CI 2
- Choix des 4 métriques CI 3
- Implémentation des tests 3
- Conclusion 4

### Introduction

Le but de ce laboratoire est de conteneuriser l'application de Oxygène CS et de mettre en place un système d'intégration continue. Pour ce faire nous avons créé des varables d'environnement pour pouvoir lancer l'application à partir de n'importe quelle habitation. Nous avons ensuite mis en place une sauvegarde de donnes de l'application HVAC dans une table de la base de données fournie. De plus, nous avons conteneurisé cette application avec Docker et créé des systèmes d'intégration continue comme des pre-commit git hooks, des tests automatisés et des métriques pour visualiser cet intégration continue.

### Répartition du travail

Nous avons divisé le travail en plusieurs morceaux en ajoutant et en assignant des tâches dans le Kanban du lab précédent pour le milestone du laboratoire 2. Nous avons séparé le laboratoire en trois parties principales. D'abord, la conteneurisation avec Docker. Puis, l'implémentation de la sauvegarde dans la base de données des informations reçues à partir du HVAC ainsi que les tests unitaires. Enfin, les quatre métriques CI pour suivre le fonctionnement du workflow. Chaque membre de l'équipe a pris une partie pour l'implémentation et l'a documentée dans le rapport.

### Implémentation de la sauvegarde des données de température dans la base de données.

Tout d'abord, nous avons mis les informations requises pour se connecter à la base de données ainsi que des informations telles que la température minimale et maximale dans des variables d'environnement. Ensuite, nous récupérons ces informations et sommes capables de nous connecter à la base de données lors du lancement de l'application. L'application va ensuite chercher les informations du capteur concernant la température ainsi que le timestamp à chaque 10 ticks, puis utilisera la fonction `save_event_to_database` pour récupérer ces informations et les mettre dans la base de données.

### Pre-commit githooks

Nous avons implémenté des pre-commit githooks pour vérifier les commit avant de les push. De plus, on a ajouté un fichier .pre-commit-config.yaml avec deux githooks. Le premier hook est le formateur Python black qui améliore le code avant de le commit. Le deuxième, Pylint, est un analyseur de code statique qui trouve des erreurs dans le code sans l'exécuter.

### Implémentation CI

Notre répertoire github contient 4 actions:

#### &nbsp;&nbsp;1. Run Test Script

&nbsp;&nbsp;&nbsp;&nbsp; Cette action est est lancé pour les push et les pull request. Elle lance les tests unitaires dans `./test/test.py`.

#### &nbsp;&nbsp;2. Pylint

&nbsp;&nbsp;&nbsp;&nbsp; Le linter `pylint` est executé pour tous les push et les pull request.

#### &nbsp;&nbsp;3. Docker image build

&nbsp;&nbsp;&nbsp;&nbsp; Lorsqu'un commit est push sur une branche ou lors d'un pull request, cette action est executé pour construire une image docker afin de s'assurer qu'il n'y a pas d'erreur.

#### &nbsp;&nbsp;4. Docker image push

&nbsp;&nbsp;&nbsp;&nbsp; Cette action est seulement executée lorsqu'il y a un push sur la branche main. Elle construit l'image docker et elle la push sur le repository docker hub avec les tags:

- latest
- \<build_number>

### Choix des 4 métriques CI

Nos métriques des builds sont faites chaque semaine, ce qui nous permet de remarquer des tendances et d'améliorer les processus.

- La première métrique que nous avons choisie est le temps moyen des builds. Ceci nous permet de voir si les builds commencent à prendre plus de temps.
- La seconde métrique que nous avons décidé d'utiliser est le temps médian des builds. Une autre métrique pour mieux comprendre si les builds ralentissent.
- La troixième métrique que nous avons ajouté est le pourcentage de succès des builds. Il est important de savoir si les builds commencent à échoués.
- Nous calculons aussi le nombre de build hebdomadaire. Ce qui nous permet de savoir si le nombre de builds augmente ou diminue au fil du temps et donc de remarquer des tendances ou des divergences.

### Implémentation des tests

Les tests seront conçus pour évaluer plusieurs aspects cruciaux de l'application. Premièrement, ils vérifieront la connexion à la base de données, s'assurant ainsi que l'application peut établir une communication stable et fiable avec le système de stockage des données. Ensuite, les tests évalueront l'insertion des données envoyées par le capteur de température, garantissant que les informations recueillies sont correctement enregistrées dans la base de données avec précision et intégrité. De plus, ils incluront la vérification de la suppression des données insérées par les tests, assurant ainsi que le processus de nettoyage fonctionne correctement pour maintenir la cohérence des données. Enfin, les tests concluront en fermant la connexion avec la base de données, clôturant ainsi le cycle complet de l'application. Cette approche de test exhaustive permettra également d'évaluer la robustesse du système dans des scénarios divers, garantissant sa fiabilité et sa performance dans des conditions variées d'utilisation.

### Conclusion

En conclusion, nous avons conteneurisé oxygencs avec Docker et établi un pipeline de déploiement pour celui-ci. Nous avons aussi sauvegardé les informations reçues de oxygencs dans la base de données fournie. Puis, nous avons ajouté du code au projet métriques pour calculer et sauvegarder quatre nouvelles "métriques" par rapport au workflow CI de oxygencs que nous avons implémenté.
