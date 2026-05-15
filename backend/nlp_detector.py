# ============================================================
#  nlp_detector.py — VERSION MAROC
#  Détection de domaine : français juridique + darija translittérée
#  Extraction d'entités : montants en MAD/DH + durées
# ============================================================

import re
from typing import Optional


class NLPDetector:
    """
    Détecteur de domaine juridique par mots-clés.
    Couvre le français juridique marocain et les termes
    darija translittérés courants.
    """

    KEYWORDS = {
        "travail": [
            # Français
            "travail", "boulot", "patron", "employeur", "licenciement", "licencié",
            "démission", "salaire", "fiche de paie", "contrat", "CDI", "CDD",
            "harcèlement", "congés", "syndicat", "ANAPEC", "rupture", "préavis",
            "indemnité", "inspection du travail", "bulletin de paie",
            "heures supplémentaires", "accident du travail", "tribunal du travail",
            # Darija translittérée
            "khedma", "maalem", "khlas", "ujra", "rassed", "tassarouh",
            "patron diali", "salaire machi wasel"
        ],
        "logement": [
            # Français
            "logement", "appartement", "maison", "loyer", "propriétaire", "bail",
            "location", "expulsion", "caution", "dépôt de garantie", "insalubre",
            "travaux", "agence immobilière", "locataire", "huissier", "résiliation",
            "état des lieux", "quittance", "commandement de payer", "tird",
            # Darija translittérée
            "dar", "kira", "malik", "sakan", "kiraa", "ijar", "wadiaa"
        ],
        "famille": [
            # Français
            "famille", "mariage", "divorce", "moudawwana", "pension", "enfant",
            "garde", "héritage", "succession", "adoption", "conjoint", "épouse",
            "séparation", "pension alimentaire", "tutelle", "tribunal de la famille",
            # Arabe / Darija courants
            "adoul", "khol", "nafaqa", "hadana", "talaq", "mirath",
            "mubara'a", "chiqaq", "wilaya", "fara'id", "tatliq", "zawaj"
        ],
        "consommateur": [
            # Français
            "achat", "vendeur", "produit", "internet", "arnaque", "escroquerie",
            "remboursement", "garantie", "vice caché", "consommation", "magasin",
            "facture", "service client", "livraison", "retour", "DPCI",
            "clause abusive", "rétractation", "e-commerce", "commande en ligne",
            # Darija translittérée
            "chtira", "bdia", "daman", "moustahlik", "ghachi", "machi zwina"
        ],
        "routier": [
            # Français
            "route", "voiture", "permis", "amende", "pv", "radar", "accident",
            "assurance auto", "points", "vitesse", "infraction", "stationnement",
            "alcool", "NARSA", "gendarmerie", "permis de conduire",
            "retrait de permis", "code de la route", "stupéfiants", "constat",
            # Darija translittérée
            "sayara", "rkhsa", "ghrama", "had9 tareeq", "permis dyali", "tomobile"
        ]
    }

    def detect_domain(self, text: str) -> Optional[str]:
        """
        Analyse le texte libre et retourne le domaine juridique
        le plus probable, ou None si aucun mot-clé trouvé.

        Args:
            text: description du problème par l'utilisateur

        Returns:
            str: clé de domaine ou None
        """
        text_lower = text.lower()
        scores = {domain: 0 for domain in self.KEYWORDS}

        for domain, keywords in self.KEYWORDS.items():
            for kw in keywords:
                if kw.lower() in text_lower:
                    scores[domain] += 1

        best_score = max(scores.values())
        if best_score > 0:
            return max(scores, key=scores.get)
        return None

    def extract_entities(self, text: str) -> dict:
        """
        Extraction d'entités : montants en MAD/DH, euros (MRE), durées.

        Args:
            text: texte de l'utilisateur

        Returns:
            dict avec les clés : amount_mad, amount_eur, duration
        """
        entities = {}

        # Montants en MAD / Dirhams
        amount_mad = re.search(
            r"(\d+(?:[.,]\d+)?)\s*(?:MAD|DH|dh|dirhams?|درهم)",
            text, re.IGNORECASE
        )
        if amount_mad:
            entities["amount_mad"] = float(amount_mad.group(1).replace(",", "."))

        # Montants en euros (cas des MRE — Marocains Résidant à l'Étranger)
        amount_eur = re.search(
            r"(\d+(?:[.,]\d+)?)\s*(?:€|euros?)",
            text, re.IGNORECASE
        )
        if amount_eur:
            entities["amount_eur"] = float(amount_eur.group(1).replace(",", "."))

        # Durées (ex : "3 mois", "2 ans", "15 jours")
        duration = re.search(
            r"(\d+)\s*(mois|ans?|années?|jours?|semaines?)",
            text, re.IGNORECASE
        )
        if duration:
            entities["duration"] = {
                "value": int(duration.group(1)),
                "unit": duration.group(2).lower()
            }

        return entities