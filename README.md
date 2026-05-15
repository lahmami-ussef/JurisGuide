# ⚖️ JurisGuide — Système Expert d'Orientation Juridique

JurisGuide est une application intelligente conçue pour aider les citoyens à comprendre leurs droits et à s'orienter dans les démarches juridiques complexes sans jargon.

## 🚀 Fonctionnalités

- **Moteur d'Inférence** : Utilise la bibliothèque `experta` pour appliquer des règles juridiques précises.
- **5 Domaines Clés** : Travail, Logement, Famille, Consommation, Routier.
- **Interface Conversationnelle** : Un bot qui vous guide pas à pas.
- **Résultats Structurés** : Badge d'urgence, liste de droits, étapes à suivre et contacts.
- **Génération de Documents** : Création automatique de lettres types (contestation, mise en demeure, etc.).

## 🛠️ Installation Locale

### 1. Backend (Python/FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate sur Windows
pip install -r requirements.txt
python main.py
```
L'API sera disponible sur `http://localhost:8000`.

### 2. Frontend (React/Vite)

```bash
cd frontend
npm install
npm run dev
```
L'application sera disponible sur `http://localhost:5173` (ou `3000` via Docker).

## 🐳 Lancement avec Docker

```bash
docker-compose up --build
```

## 🏗️ Structure du Projet

```text
JurisGuide/
├── backend/
│   ├── main.py              # Point d'entrée FastAPI
│   ├── inference_engine.py  # Moteur de règles (Experta)
│   ├── knowledge_base.py    # Questions, délais et lettres types
│   ├── session_manager.py   # Gestion de l'état en mémoire
│   └── nlp_detector.py      # Détection de domaine simple
├── frontend/
│   ├── src/
│   │   ├── components/      # UI (Chat, Result, Selector)
│   │   ├── hooks/           # Logique métier React
│   │   └── App.jsx          # Orchestration
│   └── tailwind.config.js   # Design system (Gold & Dark)
```

## 🌐 Déploiement

- **Backend** : Déployable sur Render.com ou Heroku (nécessite un `Procfile` ou configuration Docker).
- **Frontend** : Déployable sur Vercel ou Netlify. Assurez-vous de configurer `VITE_API_URL`.

---
*Avertissement : JurisGuide est un outil pédagogique et ne remplace en aucun cas les conseils d'un avocat.*
