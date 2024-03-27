# Remise de Laboratoire 3

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
- Implémentation CI 2
- Conclusion 3

### Introduction

Ce laboratoire vise à finaliser la mise en place d'un pipeline d'intégration et de déploiement continu ainsi que le monitoring de données pour la compagnie Oxygène Software. À travers ce processus, nous utiliserons Kubernetes et kubectl pour configurer et déployer le HVAC Controller et le MetricsAPI sur un cluster Kubernetes. Notre objectif est de rendre ces applications disponibles et scalables, tout en assurant leur accessibilité. Nous mettrons également en place des métriques grâce à Grafana pour pouvoir analyser les données générées. En parallèle, nous automatiserons le déploiement des nouvelles versions des applications concernées, en suivant les bonnes pratiques de développement telles que les pull-requests, la structure de branche et le kanban.

### Répartition du travail

Pour la répartition des tâches, nous avons tout d'abord défini en équipe les différentes étapes à réaliser durant ce laboratoire sur notre tableau Kanban, ainsi que la création des étiquettes, en spécifiant leur description et leur priorité. Ensuite, pour la mise en place de Kubernetes, un membre de notre équipe s'est chargé de configurer le cluster Kubernetes en utilisant le fichier de configuration kubeconfig.yaml fourni. Il a également déployé les ressources nécessaires telles que les ConfigMap et les Secrets pour garantir le bon fonctionnement de nos applications. Par la suite, un autre membre de l'équipe s'est concentré sur la configuration des métriques dans Grafana. Il a pris en charge la mise en place des paramètres appropriés et s'est assuré que les données affichées dans Grafana correspondaient correctement aux métriques collectées. En parallèle, un troisième membre de l'équipe s'est penché sur la rédaction du rapport final. Il a travaillé sur l'implémentation des métriques dans la base de données, en veillant à ce qu'elles soient correctement enregistrées. De plus, il a réalisé les tests unitaires en Python nécessaires pour s'assurer du bon fonctionnement de l'ensemble du système.

### Grafana

Nous avons ajouté nos métriques sur la plateforme de visualisation de données Grafana. Pour ce faire, nous avons connecté notre base de données directement avec Grafana. Nous avons ensuite ajouté les colonnes intérrssantes comme la température et le status du HVAC à des graphes.

### Implémentation CI



### Conclusion
