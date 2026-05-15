KNOWLEDGE_BASE = {
    "travail": {
        "questions": [
            {
                "text": "Quel est votre type de contrat ?",
                "options": ["CDI", "CDD", "Intérim", "Apprentissage"],
                "fact_key": "contrat"
            },
            {
                "text": "Depuis combien de temps travaillez-vous dans cette entreprise ?",
                "options": ["Moins de 6 mois", "6 mois à 2 ans", "Plus de 2 ans"],
                "fact_key": "anciennete"
            },
            {
                "text": "Quel est votre problème principal ?",
                "options": ["Licenciement", "Harcèlement", "Démission", "Salaires impayés"],
                "fact_key": "probleme"
            },
            {
                "text": "Avez-vous reçu une notification officielle (lettre LRAR) ?",
                "options": ["Oui", "Non, juste un SMS", "Non, oralement"],
                "fact_key": "notification"
            },
            {
                "text": "Avez-vous des preuves écrites ou témoignages ?",
                "options": ["Oui", "Non"],
                "fact_key": "preuve"
            }
        ]
    },
    "logement": {
        "questions": [
            {
                "text": "Quelle est la situation ?",
                "options": ["Expulsion", "Indécence", "Caution non rendue", "Augmentation de loyer"],
                "fact_key": "probleme"
            },
            {
                "text": "Avez-vous reçu un commandement de payer par huissier ?",
                "options": ["Oui", "Non"],
                "fact_key": "commandement_payer"
            },
            {
                "text": "Le propriétaire a-t-il été prévenu par écrit ?",
                "options": ["Oui", "Non"],
                "fact_key": "proprietaire_alerte"
            }
        ]
    },
    "famille": {
        "questions": [
            {
                "text": "Sujet de votre demande ?",
                "options": ["Divorce", "Pension", "Garde d'enfants", "Succession"],
                "fact_key": "probleme"
            },
            {
                "text": "Y a-t-il un accord entre les deux parties ?",
                "options": ["Oui", "Non"],
                "fact_key": "accord"
            },
            {
                "text": "Depuis combien de temps la pension est-elle impayée ?",
                "options": ["Moins de 1 mois", "1 à 2 mois", "> 2 mois"],
                "fact_key": "impayee"
            }
        ]
    },
    "consommateur": {
        "questions": [
            {
                "text": "De quel type de litige s'agit-il ?",
                "options": ["Achat Internet", "Arnaque", "Vices cachés voiture", "Abus de faiblesse"],
                "fact_key": "probleme"
            },
            {
                "text": "Depuis combien de temps avez-vous reçu le produit ?",
                "options": ["< 14 jours", "14 jours à 2 ans", "> 2 ans"],
                "fact_key": "delai"
            },
            {
                "text": "Quel est le montant approximatif du préjudice ?",
                "options": ["< 100€", "100€ à 1000€", "> 1000€"],
                "fact_key": "montant"
            }
        ]
    },
    "routier": {
        "questions": [
            {
                "text": "Quel est l'objet de votre demande ?",
                "options": ["PV", "Permis", "Accident", "Alcoolémie/Stupéfiants"],
                "fact_key": "probleme"
            },
            {
                "text": "Combien de points reste-t-il sur votre permis ?",
                "options": ["12", "1 à 11", "0"],
                "fact_key": "points"
            },
            {
                "text": "Avez-vous déjà payé l'amende ?",
                "options": ["Oui", "Non"],
                "fact_key": "conteste"
            }
        ]
    }
}
