# ============================================================
#  knowledge_base.py — VERSION MAROC
#  Lois : Code du Travail 65-99 | Loi 67-12 | Moudawwana 70-03
#         Loi 31-08 | Code de la Route 52-05
# ============================================================

KNOWLEDGE_BASE = {

    # --------------------------------------------------------
    #  TRAVAIL — Loi n° 65-99
    # --------------------------------------------------------
    "travail": {
        "questions": [
            {
                "text": "Quel est votre type de contrat ?",
                "options": ["CDI", "CDD", "Intérim", "ANAPEC"],
                "fact_key": "contrat"
            },
            {
                "text": "Depuis combien de temps travaillez-vous dans cette entreprise ?",
                "options": ["Moins de 6 mois", "6 mois à 2 ans", "Plus de 2 ans"],
                "fact_key": "anciennete"
            },
            {
                "text": "Quel est votre problème principal ?",
                "options": ["Licenciement", "Harcèlement", "Salaires impayés", "Accident de travail"],
                "fact_key": "probleme"
            },
            {
                "text": "Avez-vous reçu une notification officielle ?",
                "options": ["Lettre recommandée", "Verbal seulement", "Rien reçu"],
                "fact_key": "notification"
            },
            {
                "text": "Avez-vous des preuves (contrat, bulletins de paie, témoins) ?",
                "options": ["Oui", "Non"],
                "fact_key": "preuve"
            }
        ]
    },

    # --------------------------------------------------------
    #  LOGEMENT — Loi n° 67-12
    # --------------------------------------------------------
    "logement": {
        "questions": [
            {
                "text": "Quelle est votre situation ?",
                "options": ["Expulsion", "Loyer impayé", "Insalubrité / Dégradations", "Caution non rendue"],
                "fact_key": "probleme"
            },
            {
                "text": "Avez-vous un contrat de bail écrit ?",
                "options": ["Oui, contrat écrit", "Non, accord verbal"],
                "fact_key": "contrat_ecrit"
            },
            {
                "text": "Avez-vous reçu un commandement d'huissier ?",
                "options": ["Oui", "Non"],
                "fact_key": "commandement_payer"
            },
            {
                "text": "Le propriétaire a-t-il été prévenu par écrit ?",
                "options": ["Oui", "Non"],
                "fact_key": "proprietaire_alerte"
            },
            {
                "text": "Depuis combien de temps le loyer est-il impayé ?",
                "options": ["Moins de 1 mois", "1 à 3 mois", "Plus de 3 mois"],
                "fact_key": "impaye_duree"
            }
        ]
    },

    # --------------------------------------------------------
    #  FAMILLE — Moudawwana (Loi n° 70-03)
    # --------------------------------------------------------
    "famille": {
        "questions": [
            {
                "text": "Quel est le sujet de votre demande ?",
                "options": ["Divorce", "Pension alimentaire", "Garde d'enfants", "Héritage / Succession"],
                "fact_key": "probleme"
            },
            {
                "text": "Y a-t-il un accord entre les deux parties ?",
                "options": ["Oui", "Non"],
                "fact_key": "accord"
            },
            {
                "text": "Y a-t-il des enfants mineurs ?",
                "options": ["Oui", "Non"],
                "fact_key": "enfants"
            },
            {
                "text": "Depuis combien de temps la pension est-elle impayée ?",
                "options": ["Moins de 1 mois", "1 à 3 mois", "Plus de 3 mois"],
                "fact_key": "impayee"
            },
            {
                "text": "Le mariage est-il officiellement enregistré ?",
                "options": ["Acte adoulaire enregistré", "Non enregistré"],
                "fact_key": "type_mariage"
            }
        ]
    },

    # --------------------------------------------------------
    #  CONSOMMATEUR — Loi n° 31-08
    # --------------------------------------------------------
    "consommateur": {
        "questions": [
            {
                "text": "De quel type de litige s'agit-il ?",
                "options": ["Achat Internet", "Arnaque / Escroquerie", "Vice caché", "Clause abusive"],
                "fact_key": "probleme"
            },
            {
                "text": "Depuis combien de temps avez-vous reçu le produit / service ?",
                "options": ["Moins de 7 jours", "7 jours à 2 ans", "Plus de 2 ans"],
                "fact_key": "delai"
            },
            {
                "text": "Quel est le montant approximatif du préjudice ?",
                "options": ["Moins de 500 MAD", "500 à 5000 MAD", "Plus de 5000 MAD"],
                "fact_key": "montant"
            },
            {
                "text": "Avez-vous envoyé une mise en demeure au vendeur ?",
                "options": ["Oui", "Non"],
                "fact_key": "mise_demeure"
            },
            {
                "text": "Le vendeur est-il un professionnel ou un particulier ?",
                "options": ["Professionnel / Société", "Particulier"],
                "fact_key": "vendeur_type"
            }
        ]
    },

    # --------------------------------------------------------
    #  ROUTIER — Loi n° 52-05
    # --------------------------------------------------------
    "routier": {
        "questions": [
            {
                "text": "Quel est l'objet de votre demande ?",
                "options": ["PV / Amende", "Retrait de permis", "Accident", "Alcool / Drogues"],
                "fact_key": "probleme"
            },
            {
                "text": "Combien de points reste-t-il sur votre permis ?",
                "options": ["30 points (plein)", "1 à 29 points", "0 point"],
                "fact_key": "points"
            },
            {
                "text": "Avez-vous déjà payé l'amende ?",
                "options": ["Oui", "Non"],
                "fact_key": "conteste"
            },
            {
                "text": "Y a-t-il des blessés dans l'accident ?",
                "options": ["Oui", "Non", "Sans objet"],
                "fact_key": "blesses"
            },
            {
                "text": "Un taux d'alcoolémie a-t-il été constaté officiellement ?",
                "options": ["Oui", "Non"],
                "fact_key": "alcoolemie"
            }
        ]
    }
}