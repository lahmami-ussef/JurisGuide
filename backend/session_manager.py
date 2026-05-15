from typing import Dict, Any, Optional

class SessionManager:
    """Gère les sessions utilisateur en mémoire."""
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self, session_id: str, domain: Optional[str] = None):
        """Initialise une nouvelle session."""
        self.sessions[session_id] = {
            "domain": domain,
            "facts": {}, # les reponses 
            "step": 0,
            "history": []
        }

    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Récupère les données d'une session."""
        return self.sessions.get(session_id)

    def update_session(self, session_id: str, **kwargs):
        """Met à jour les champs d'une session."""
        # **kwargs signfie n'importe quels champs 
        if session_id in self.sessions:
            self.sessions[session_id].update(kwargs)

    def add_fact(self, session_id: str, key: str, value: Any):
        """Ajoute un fait à la session."""
        if session_id in self.sessions:
            self.sessions[session_id]["facts"][key] = value
