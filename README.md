
# 🧮 RPN Calculator API – FastAPI + Docker + PostgreSQL

## 🎯 Objectif

Ce projet propose la création d'une **API REST de calculatrice en Notation Polonaise Inverse (RPN)**.
L’objectif est d’aider nos utilisateurs à effectuer des calculs complexes tout en conservant l’historique des opérations en base de données.
L’application doit également permettre l’**export CSV** des résultats.

Le projet est découpé et géré selon une méthodologie **Scrum** avec des **tickets estimés en story points Fibonacci**.

---

## 📅 Durée & Organisation

- **Sprint unique** : 8 jours
- **Start**: Lundi 16 Juin 2025
- **End**: Mercredi 25 Juin 2025

> 🎲 1 Story Point = 1 jour de travail
>
> Suite Fibonacci utilisée : 1, 2, 3, 5, 8...

---

## 🧑‍🤝‍🧑 Équipe projet

| Rôle           | Nom / Référence             | Missions principales                         |
|----------------|-----------------------------|----------------------------------------------|
| Tech Lead      | [John Doe]                  | Architecture, revues, guidage métier         |
| Dev Backend    | Développeur Python Junior   | Implémentation de l’algo, API                |
| DevOps         | Ingénieur Infrastructure    | Docker, PostgreSQL, CI/CD                    |
| Scrum Master   | Scrum Master / Tech Lead    | Suivi d'avancement, daily, coordination      |

---

## 📋 Responsabilités clés

### 👨‍💻 Tech Lead Python

- Choix techniques (FastAPI, PostgreSQL, SQLAlchemy, etc.)

- Revue de code et pair programming

- Garant des principes SOLID, KISS, YAGNI

- Définition de l’architecture modulaire : séparation des couches (API, services, persistance)

### 🧑‍🏫 Scrum Master

- Animation des daily stand-up, sprint planning & retro

- Suivi du burn-down chart

- Mise en place du kanban/scrum board (ex : Jira, Notion, Trello)

### 🧑‍💻 DevOps Engineer

- Écriture des Dockerfiles

- Configuration docker-compose

- Configuration PostgreSQL, gestion des volumes

- CI/CD (ex : GitHub Actions)

---

## 🧱 Organisation technique

### 📁 Arborescence Clean Architecture (inspirée SOLID)

```arduino
app/
├── github/              # intégration GitHub (actions, workflows)
│   ├── workflows/
│   │   ├── ci.yml
├── api/                 # routes FastAPI
│   ├── routes.py
├── core/             # logique métier (calcul NPI)
│   ├── rpn.py
├── db/               # modèles ORM, sessions
│   ├── database.py
├── models/               # modèles ORM, sessions
│   ├── models.py
├── schemas/          # pydantic schemas
│   ├── schemas.py
├── services/         # services métier
│   ├── services.py
tests/
├── test_integration.py
├── test_rpn.py
.env
docker-compose.yml
Dockerfile
example.env
main.py
README.md
requirements.txt
wait-for-db.sh
```

## 📦 Fonctionnalités

- Calcul RPN (notation polonaise inverse)
- API REST FastAPI
- Stockage en PostgreSQL
- Export CSV
- Conteneurisation Docker avec Docker Compose

---

## 🗂️ Découpage en tickets

| ID    | Titre                                      | Story Points | Due Date  | Critères d’acceptation |
|-------|--------------------------------------------|--------------|-----------|--------------------------|
| T1    | Initialisation projet + structure Clean     | 1 SP         | 16/06     | Projet FastAPI structuré en dossiers `api`, `core`, `schemas`, etc. Fichier `.env` en place |
| T2    | Implémentation de l’algorithme RPN         | 2 SP         | 17/06     | La fonction `rpn_calculator(expr)` gère `+`, `-`, `*`, `/` et retourne le bon résultat |
| T3    | Création des schémas Pydantic              | 1 SP         | 17/06     | Les schémas `OperationRequest` et `OperationResponse` valident correctement les inputs |
| T4    | Route POST /calculate                      | 2 SP         | 18/06     | Reçoit une expression, retourne un JSON avec le résultat. Gère les erreurs |
| T5    | Création des modèles ORM SQLAlchemy        | 2 SP         | 18/06     | Modèle `Operation(id, expression, result)` persisté via PostgreSQL |
| T6    | Ajout du service de persistance            | 3 SP         | 19/06     | Résultats bien stockés et récupérés dans la base après un calcul |
| T7    | Route GET /export (CSV)                    | 2 SP         | 20/06     | Fichier CSV bien généré avec les colonnes `ID, Expression, Result`, téléchargeable |
| T8    | Dockerisation de l’app FastAPI             | 2 SP         | 21/06     | Dockerfile fonctionnel. Démarrage avec `uvicorn` depuis Docker |
| T9    | docker-compose pour PostgreSQL + API       | 3 SP         | 22/06     | `docker-compose up` démarre l’API et la BDD avec persistance locale |
| T10   | Documentation technique (README + Swagger) | 1 SP         | 23/06     | README complet, endpoints documentés via `/docs` (Swagger) |
| T11   | Export CSV : tests fonctionnels            | 1 SP         | 24/06     | CSV validé, testé avec au moins 5 expressions en base |
| T12   | Tests unitaires + intégration CI GitHub    | 3 SP         | 25/06     | Tests du calcul, des routes API, des erreurs. CI intégrée avec `pytest` via GitHub Actions |

---

## ✅ Critères de succès globaux

- Tous les tickets validés
  - Tous les tests passent pour chaque fonctionnalité
- Documentation complète et à jour
- Projet fonctionnel via `http://localhost:8000/docs`
- Résultats persistés dans PostgreSQL
- Dockerisé et exécutable via `docker-compose`
- Couverture de test minimale sur le calcul et les endpoints
- Export CSV complet et lisible

---

## 🔧 Lancement rapide

### 📦 Prérequis

- Docker / Docker Compose
- Python 3.10+ (pour les tests locaux)
- Git

### ▶️ Exécution

```bash
docker-compose up --build
```

### 📂 Accès aux endpoints

- **Documentation Swagger**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **API**: [http://localhost:8000/api/v1](http://localhost:8000/api/v1)

### 🧪 Tester en local

```bash
curl -X POST "http://localhost:8000/calculate" -H "Content-Type: application/json" -d '{"expression": "5 1 2 + 4 * + 3 -"}'
```

Réponse attendue :

```json
{
  "expression": "5 1 2 + 4 * + 3 -",
  "result": 14.0
}
```

### 📁 Export CSV

```bash
curl -X GET "http://localhost:8000/export" -H "Accept: text/csv"
```

Réponse attendue : fichier CSV téléchargeable avec les opérations effectuées.

### 🤝 Contributions

Pour toute contribution, merci de :

Créer une branche au même nom que le ticket `rnp-t<ID>`
Chaque commit doit être lié à un ticket Jira et suivre le format `rnp-t<ID> - Description du commit`
Faire une PR vers la branche `dev`

Suivre le style de code (formatage Black + type hints)

Écrire des tests unitaires pour toute logique métier

Pour run le projet en local, créer un environnement virtuel et un fichier `.env` à la racine et remplacer les valeurs par défaut (assurez-vous d'avoir PostgreSQL installé et en cours d'exécution) :

```bash
cp example.env .env
```

PS:

- Assurez-vous d'avoir les dépendances installées via `pip install -r requirements.txt` avant de lancer le projet.

- La containerisation avec Docker sera faite en pair avec le DevOps Engineer/Tech Lead pour une montée en compétences.

### 👨‍🔧 Mainteneur

Tech Lead : John Doe
Contact : [john.doe@projet.dev](mailto:john.doe@projet.dev)
