# Résumé de la Vidéo sur Docker et SQL
## Introduction à Docker Compose
- Docker Compose permet de configurer plusieurs conteneurs dans un seul fichier YAML, simplifiant la gestion de réseaux partagés et de configurations.
- Avantage : réduit la complexité des commandes Docker pour exécuter plusieurs services.

## Installation de Docker Compose
- **Mac et Windows** : Docker Compose est inclus avec Docker Desktop.
- **Linux** : Nécessite une installation manuelle.

## Configuration avec Docker Compose
- Création d'un fichier `docker-compose.yaml` pour configurer PostgreSQL et pgAdmin.
- **Services configurés** :
  - **PostgreSQL** : définition de l'image, variables d'environnement, mappages de volumes, et mappages de ports.
  - **pgAdmin** : définition de l'image, variables d'environnement, et mappages de ports.

## Exécution avec Docker Compose
- Lancement des services avec la commande `docker-compose up`.
- Accès à pgAdmin via un navigateur pour se connecter à la base de données PostgreSQL.

## Commandes Importantes
- **Lancer Docker Compose** : `docker-compose up`
- **Arrêter Docker Compose** : `docker-compose down`
- **Mode détaché** : Ajouter l'option `-d` pour exécuter en arrière-plan. `docker-compose up -d`

## Avantages de Docker Compose
- Simplifie la gestion de configurations multiples.
- Facilite les expériences locales et les tests d'intégration.