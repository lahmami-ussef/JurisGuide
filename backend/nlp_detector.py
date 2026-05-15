import re # modele pour les expression regulieres 
from typing import Optional

class NLPDetector:
    """Détecteur de domaine par mots-clés et expressions régulières."""
    
    KEYWORDS = {
        "travail": [
            "travail", "boulot", "patron", "employeur", "licenciement", "licencié",
            "démission", "salaire", "fiche de paie", "contrat", "CDI", "CDD",
            "prudhommes", "harcèlement", "congés", "syndicat"
        ],
        "logement": [
            "logement", "appartement", "maison", "loyer", "propriétaire", "bail",
            "location", "expulsion", "caution", "dépôt de garantie", "insalubre",
            "travaux", "agence immobilière", "adil"
        ],
        "famille": [
            "famille", "mariage", "divorce", "pacs", "pension", "enfant", "garde",
            "héritage", "succession", "adoption", "parent", "conjoint", "ex-mari"
        ],
        "consommateur": [
            "achat", "vendeur", "produit", "internet", "arnaque", "escroquerie",
            "remboursement", "garantie", "vice caché", "consommation", "magasin",
            "facture", "service client"
        ],
        "routier": [
            "route", "voiture", "permis", "amende", "pv", "radar", "accident",
            "assurance auto", "points", "vitesse", "infraction", "stationnement"
        ]
    }

    def detect_domain(self, text: str) -> Optional[str]:
        """Analyse le texte pour détecter le domaine juridique le plus probable."""

        text = text.lower() # minuscule 

        scores = {domain: 0 for domain in self.KEYWORDS} # 0 pour chaque domaine
        
        for domain, keywords in self.KEYWORDS.items(): # for damain and kw 
            for kw in keywords: # if kw in domain kw in text 
                if kw in text: # if in text
                    scores[domain] += 1 # raise score
        
        # Trouver le domaine avec le score maximum
        if max(scores.values()) > 0: # 
            return max(scores, key=scores.get) # return domain with max score 
            
        
        return None

    def extract_entities(self, text: str):
        """Extraction basique d'entités (Dates, Montants)."""
        entities = {}
        
        # Extraction de montants (ex: 100€, 100 euros)
        amount_match = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:€|euros?)", text, re.IGNORECASE)
        if amount_match:
            entities["amount"] = float(amount_match.group(1).replace(",", "."))
            
        return entities
