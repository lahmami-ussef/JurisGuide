import collections

# Résolution d'un problème de compatibilité avec les versions récentes de Python (3.10+)
# La bibliothèque experta utilise "collections.Mapping" qui a été déplacé dans "collections.abc"
if not hasattr(collections, 'Mapping'):
    import collections.abc
    collections.Mapping = collections.abc.Mapping

from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uuid

# Importation de nos propres modules métier
from inference_engine import JurisInference
from session_manager import SessionManager
from nlp_detector import NLPDetector
from knowledge_base import KNOWLEDGE_BASE


# 1. CRÉATION DE L'API FASTAPI

# Instanciation de l'application. FastAPI génère automatiquement
# une documentation interactive accessible sur http://localhost:8000/docs
app = FastAPI(title="JurisGuide API", version="1.0.0")


# 2. MIDDLEWARES (CORS)

# Le CORS (Cross-Origin Resource Sharing) est configuré ici pour permettre
# à notre frontend React (qui tourne sur le port 5173) de faire des requêtes
# HTTP vers ce backend Python (qui tourne sur le port 8000).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # En production, on mettrait ["http://localhost:5173"]
    allow_credentials=True,  
    allow_methods=["*"],     # Autorise toutes les requêtes (GET, POST...)
    allow_headers=["*"],     
)


# 3. INSTANCIATION DES SERVICES

# On crée les objets qui vont gérer la logique métier globale
session_manager = SessionManager() # Gère les sessions utilisateurs et leurs réponses
nlp_detector = NLPDetector()       # Analyse le texte pour trouver le bon domaine juridique



# 4. MODÈLES DE DONNÉES (PYDANTIC)

# Ces classes définissent le format JSON que l'API s'attend à recevoir.
# Si le JSON reçu ne correspond pas, FastAPI renvoie une erreur 422 automatiquement.

class ChatRequest(BaseModel):
    session_id: str   # Identifiant de la session de chat
    message: str      # Le texte ou l'option choisie par l'utilisateur

class StartRequest(BaseModel):
    domain: Optional[str] = None  # Le domaine (ex: "travail", "logement") - Peut être vide



# 5. DÉFINITION DES ROUTES (ENDPOINTS)

# --- Route de base ---
@app.get("/")
async def root():
    """Affiche un message d'accueil pour confirmer que le serveur tourne."""
    return {
        "message": "Bienvenue sur l'API JurisGuide",
        "status": "online",
        "endpoints": {
            "health": "/api/health",
            "domains": "/api/domains"
        }
    }

# --- Route de santé (Health Check) ---
@app.get("/api/health")
async def health_check():
    """Route technique pour vérifier que le service est sain."""
    return {"status": "healthy", "service": "JurisGuide"}

# --- Route des domaines ---
@app.get("/api/domains")
async def get_domains():
    """Renvoie la liste des domaines juridiques supportés par l'application."""
    return [
        {"id": "travail", "label": "Droit du travail", "icon": "💼"},
        {"id": "logement", "label": "Droit du logement", "icon": "🏠"},
        {"id": "famille", "label": "Droit de la famille", "icon": "👨‍👩‍👧‍👦"},
        {"id": "consommateur", "label": "Droit du consommateur", "icon": "🛒"},
        {"id": "routier", "label": "Droit routier", "icon": "🚗"},
    ]


# --- Route de démarrage de session ---
@app.post("/api/start")
async def start_session(request: StartRequest):
    """
    Cette route est appelée quand l'utilisateur clique sur un domaine.
    Elle initialise une session et renvoie la toute première question.
    """
    # 1. Création d'un ID unique pour reconnaitre l'utilisateur
    session_id = str(uuid.uuid4()) 
    
    # 2. Sauvegarde de la session en mémoire
    session_manager.create_session(session_id, request.domain) 
    
    response_msg = "Bonjour ! Je suis JurisGuide. "
    
    # 3. Si un domaine a été sélectionné, on lance la première question
    if request.domain:
        first_q = KNOWLEDGE_BASE[request.domain]["questions"][0]
        return {
            "session_id": session_id,
            "message": f"{response_msg} Parlons de {request.domain}. {first_q['text']}",
            "options": first_q["options"],
            "step": 0 # L'utilisateur en est à l'étape 0 du questionnaire
        }
    
    # 4. Si aucun domaine (question libre), on demande de préciser
    return {
        "session_id": session_id,
        "message": f"{response_msg} Quel est le domaine de votre question ?",
        "step": -1
    }


# --- Route du Chat Principal ---
@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    C'est ici que transitent tous les messages de l'utilisateur.
    Gère la progression du questionnaire et déclenche le moteur d'inférence.
    """
    # ÉTAPE 1 : Vérification de sécurité
    # On s'assure que le session_id fourni existe bien dans notre SessionManager
    session = session_manager.get_session(request.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session non trouvée")

    # ÉTAPE 2 : Détection NLP (Natural Language Processing)
    # Si le domaine n'est pas encore défini, on essaie de le deviner
    # à partir du texte libre tapé par l'utilisateur.
    if not session["domain"]:
        detected_domain = nlp_detector.detect_domain(request.message)
        if detected_domain:
            # Si on a trouvé le domaine, on met à jour la session
            session_manager.update_session(request.session_id, domain=detected_domain)
            session = session_manager.get_session(request.session_id)
        else:
            # Sinon, on redemande
            return {
                "message": "Je n'ai pas bien compris le domaine. Concerne-t-il le travail, le logement, la famille, la consommation ou la route ?",
                "step": -1
            }

    # On récupère le domaine et les questions associées dans la base de connaissances
    domain = session["domain"]
    current_step = session["step"]
    questions = KNOWLEDGE_BASE[domain]["questions"]

    # ÉTAPE 3 : Sauvegarde de la réponse
    # On stocke la réponse de l'utilisateur dans le dictionnaire "facts"
    # Exemple : session["facts"]["contrat"] = "CDI"
    if current_step < len(questions):
        fact_key = questions[current_step]["fact_key"]
        session["facts"][fact_key] = request.message
        session["step"] += 1 # On incrémente l'étape
        
    # ÉTAPE 4 : Renvoi de la prochaine question
    # S'il reste des questions, on les envoie au client
    if session["step"] < len(questions):
        next_q = questions[session["step"]]
        return {
            "message": next_q["text"],
            "options": next_q.get("options", []),
            "step": session["step"]
        }
    
    # ÉTAPE 5 : Lancement du Moteur d'Inférence
    # Toutes les questions ont été posées. On analyse les faits.
    else:
        # Création du moteur d'inférence (basé sur Experta)
        engine = JurisInference()
        engine.reset() 
        
        # On déclare au moteur tous les faits (les réponses) de la session
        engine.declare_facts(domain, session["facts"])
        
        # Le moteur évalue les faits contre ses règles (les @Rule)
        engine.run()
        
        # On récupère le résultat final
        result = engine.get_result()
        
        # Règle de secours : si le cas de l'utilisateur ne correspond à aucune règle
        if not result:
            result = {
                "urgency": "orange",
                "title": "Analyse complexe requise",
                "rights": ["Votre situation nécessite une étude approfondie."],
                "steps": ["Consulter un avocat spécialisé", "Contacter une maison de justice"],
                "deadline": "Variable selon la procédure",
                "docs": []
            }
            
        # On renvoie le résultat au frontend
        # Le flag 'is_final: True' indique au React d'afficher la carte de résultat final
        return {
            "message": "J'ai analysé votre situation. Voici mes conclusions :",
            "result": result,
            "is_final": True
        }


# 6. LANCEMENT DU SERVEUR

if __name__ == "__main__":
    import uvicorn
    # Le serveur écoute sur toutes les interfaces (0.0.0.0) au port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
