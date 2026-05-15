# ============================================================
#  inference_engine.py — VERSION MAROC
#  Moteur d'inférence basé sur Experta
#  Références : Loi 65-99 | Loi 67-12 | Moudawwana 70-03
#               Loi 31-08 | Code de la Route 52-05
# ============================================================

import collections
if not hasattr(collections, 'Mapping'):
    import collections.abc
    collections.Mapping = collections.abc.Mapping

from experta import KnowledgeEngine, Rule, Fact
from typing import Dict, Any


class JurisFact(Fact):
    """Structure de fait pour JurisGuide Maroc."""
    pass


class JurisInference(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.result = None

    def declare_facts(self, domain: str, facts: Dict[str, str]):
        """Déclare les faits collectés dans le moteur."""
        self.declare(JurisFact(domain=domain, **facts))

    def get_result(self):
        return self.result

    # ============================================================
    #  DROIT DU TRAVAIL — Loi n° 65-99
    # ============================================================

    @Rule(JurisFact(domain='travail', contrat='CDI',
                    anciennete='Plus de 2 ans',
                    probleme='Licenciement',
                    notification='Verbal seulement'))
    def rule_travail_licenciement_verbal(self):
        self.result = {
            "urgency": "red",
            "title": "Licenciement Verbal — Irrégulier (Art. 62 Loi 65-99)",
            "rights": [
                "Indemnité légale : 1,5 mois de salaire par année d'ancienneté (Art. 52)",
                "Indemnité compensatrice de préavis",
                "Dommages et intérêts pour licenciement abusif"
            ],
            "steps": [
                "Ne signez aucune démission",
                "Envoyez une lettre recommandée à l'employeur pour réclamer la notification écrite",
                "Saisissez l'Inspection du Travail (DGAT)",
                "Déposez une requête au Tribunal du Travail dans les 90 jours"
            ],
            "deadline": "90 jours pour contester la rupture du contrat (Art. 396 — prescription 2 ans)",
            "contacts": [
                "Inspection du Travail : www.emploi.gov.ma",
                "Tribunal du Travail de votre ville"
            ]
        }

    @Rule(JurisFact(domain='travail', contrat='CDI',
                    anciennete='Plus de 2 ans',
                    probleme='Licenciement',
                    notification='Rien reçu'))
    def rule_travail_licenciement_sans_notification(self):
        self.result = {
            "urgency": "red",
            "title": "Licenciement Sans Notification — Nul (Art. 62 Loi 65-99)",
            "rights": [
                "Licenciement considéré comme abusif sans notification écrite",
                "Indemnité légale : 1,5 mois de salaire par année d'ancienneté (Art. 52)",
                "Réintégration possible ou dommages et intérêts"
            ],
            "steps": [
                "Continuez à vous présenter au travail ou envoyez un courrier recommandé",
                "Saisissez immédiatement l'Inspection du Travail",
                "Préparez tous vos bulletins de paie et contrat",
                "Déposez une requête au Tribunal du Travail"
            ],
            "deadline": "2 ans de prescription (Art. 396 Loi 65-99)",
            "contacts": [
                "Inspection du Travail : www.emploi.gov.ma",
                "DGAT — Direction Générale du Travail"
            ]
        }

    @Rule(JurisFact(domain='travail', contrat='CDI',
                    anciennete='Moins de 6 mois',
                    probleme='Licenciement'))
    def rule_travail_periode_essai(self):
        self.result = {
            "urgency": "orange",
            "title": "Rupture en Période d'Essai (Art. 13 Loi 65-99)",
            "rights": [
                "Aucune indemnité légale de licenciement avant 6 mois",
                "Sauf clause contractuelle plus favorable",
                "Droit au solde de tout compte complet"
            ],
            "steps": [
                "Vérifiez les clauses de votre contrat",
                "Réclamez votre solde de tout compte (salaire + congés non pris)",
                "Contactez l'Inspection du Travail en cas de non-paiement"
            ],
            "deadline": "Réclamation solde de tout compte : 2 ans (Art. 396)",
            "contacts": [
                "Inspection du Travail : www.emploi.gov.ma"
            ]
        }

    @Rule(JurisFact(domain='travail', contrat='CDD', probleme='Licenciement'))
    def rule_travail_cdd_rupture(self):
        self.result = {
            "urgency": "orange",
            "title": "Rupture Anticipée de CDD (Art. 33 Loi 65-99)",
            "rights": [
                "Dommages et intérêts égaux aux salaires restants jusqu'au terme du contrat",
                "CDD > 1 an sans motif valable = requalification possible en CDI (Art. 16)"
            ],
            "steps": [
                "Calculez le nombre de mois restants sur votre CDD",
                "Envoyez une mise en demeure à l'employeur par lettre recommandée",
                "Saisissez le Tribunal du Travail si refus de paiement"
            ],
            "deadline": "2 ans de prescription (Art. 396 Loi 65-99)",
            "contacts": [
                "Tribunal du Travail de votre ville",
                "Inspection du Travail : www.emploi.gov.ma"
            ]
        }

    @Rule(JurisFact(domain='travail', probleme='Harcèlement', preuve='Oui'))
    def rule_travail_harcelement_avec_preuve(self):
        self.result = {
            "urgency": "red",
            "title": "Harcèlement Moral au Travail — Preuves Disponibles",
            "rights": [
                "Protection contre toute mesure de représailles",
                "Résiliation judiciaire du contrat aux torts de l'employeur",
                "Plainte pénale possible (Art. 503-1 Code Pénal marocain)"
            ],
            "steps": [
                "Conservez toutes les preuves (emails, SMS, témoignages écrits)",
                "Signalez à la Direction des Ressources Humaines par écrit",
                "Déposez une plainte pénale à la gendarmerie ou la police",
                "Saisissez le Tribunal du Travail pour résiliation aux torts de l'employeur"
            ],
            "deadline": "Plainte pénale : 5 ans | Action civile : 2 ans (Art. 396)",
            "contacts": [
                "Tribunal du Travail de votre ville",
                "Inspection du Travail : www.emploi.gov.ma"
            ]
        }

    @Rule(JurisFact(domain='travail', probleme='Salaires impayés'))
    def rule_travail_salaires_impayes(self):
        self.result = {
            "urgency": "red",
            "title": "Salaires Impayés (Art. 532 Loi 65-99)",
            "rights": [
                "Droit au paiement intégral du salaire à la date convenue",
                "Intérêts de retard en cas de retard injustifié",
                "Droit de quitter l'entreprise pour faute de l'employeur"
            ],
            "steps": [
                "Envoyez une mise en demeure écrite à l'employeur",
                "Saisissez l'Inspection du Travail (DGAT) — premier recours gratuit",
                "En cas d'échec, déposez une requête au Tribunal du Travail",
                "Réclamez l'ensemble des arriérés + dommages et intérêts"
            ],
            "deadline": "Prescription : 2 ans à partir de la date d'exigibilité (Art. 396)",
            "contacts": [
                "Inspection du Travail : www.emploi.gov.ma",
                "DGAT — Direction Générale du Travail"
            ]
        }

    @Rule(JurisFact(domain='travail', probleme='Accident de travail'))
    def rule_travail_accident(self):
        self.result = {
            "urgency": "red",
            "title": "Accident de Travail (Dahir 1943 — CNSS)",
            "rights": [
                "Indemnité journalière versée par la CNSS",
                "Prise en charge médicale intégrale",
                "Rente d'incapacité permanente si séquelles",
                "L'employeur est responsable sauf faute inexcusable du salarié"
            ],
            "steps": [
                "Déclarez l'accident à l'employeur immédiatement",
                "L'employeur doit déclarer à la CNSS dans les 48h",
                "Consultez un médecin et obtenez un certificat médical initial",
                "Conservez tous les documents médicaux"
            ],
            "deadline": "Déclaration CNSS : 48 heures après l'accident",
            "contacts": [
                "CNSS : www.cnss.ma — 0522 54 23 23",
                "Inspection du Travail : www.emploi.gov.ma"
            ]
        }

    # ============================================================
    #  DROIT DU LOGEMENT — Loi n° 67-12
    # ============================================================

    @Rule(JurisFact(domain='logement', probleme='Expulsion', commandement_payer='Non'))
    def rule_logement_expulsion_sans_huissier(self):
        self.result = {
            "urgency": "red",
            "title": "Expulsion Illégale — Sans Commandement d'Huissier (Art. 21 Loi 67-12)",
            "rights": [
                "Toute expulsion sans décision judiciaire est illégale",
                "Droit à la réintégration immédiate dans le logement",
                "Droit aux dommages et intérêts"
            ],
            "steps": [
                "Saisissez le juge des référés du TPI pour réintégration d'urgence",
                "Déposez une plainte pénale contre le propriétaire (violation de domicile)",
                "Contactez l'autorité locale (moqadem / caïd) comme témoin"
            ],
            "deadline": "Recours en référé : procédure d'urgence, agissez dans les 24-48h",
            "contacts": [
                "Tribunal de Première Instance (TPI) de votre ville",
                "Commune / Arrondissement"
            ]
        }

    @Rule(JurisFact(domain='logement', probleme='Expulsion', commandement_payer='Oui'))
    def rule_logement_expulsion_avec_commandement(self):
        self.result = {
            "urgency": "orange",
            "title": "Procédure d'Expulsion Locative — Commandement Reçu (Art. 32 Loi 67-12)",
            "rights": [
                "Droit de demander des délais de grâce au juge",
                "Droit à une audience avant toute expulsion effective",
                "Possibilité d'accord amiable avec le propriétaire (plan d'apurement)"
            ],
            "steps": [
                "Préparez un plan de remboursement écrit à proposer au propriétaire",
                "Présentez-vous obligatoirement à l'audience du tribunal",
                "Demandez un délai de grâce au juge (Art. 32)",
                "Cherchez un relogement d'urgence en parallèle"
            ],
            "deadline": "Régularisation recommandée avant la date d'audience",
            "contacts": [
                "Tribunal de Première Instance (TPI)",
                "Commune / Arrondissement"
            ]
        }

    @Rule(JurisFact(domain='logement', probleme='Insalubrité / Dégradations',
                    proprietaire_alerte='Oui'))
    def rule_logement_insalubrite_alerte(self):
        self.result = {
            "urgency": "orange",
            "title": "Logement Insalubre — Propriétaire Alerté Sans Réponse (Art. 29 Loi 67-12)",
            "rights": [
                "Travaux forcés aux frais du propriétaire via décision judiciaire",
                "Réduction de loyer proportionnelle au préjudice subi",
                "Résiliation du bail aux torts du propriétaire sans frais"
            ],
            "steps": [
                "Saisissez la commune pour un constat officiel d'insalubrité",
                "Déposez une requête au TPI pour travaux forcés ou résiliation",
                "Conservez toutes les preuves (photos datées, lettres envoyées)"
            ],
            "deadline": "Agissez avant que la situation empire — aucun délai légal mais urgent",
            "contacts": [
                "Commune / Service d'Hygiène",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    @Rule(JurisFact(domain='logement', probleme='Insalubrité / Dégradations',
                    proprietaire_alerte='Non'))
    def rule_logement_insalubrite_non_alerte(self):
        self.result = {
            "urgency": "orange",
            "title": "Logement Insalubre — Étape Préalable Requise (Art. 28 Loi 67-12)",
            "rights": [
                "Droit à un logement décent",
                "Obligation légale du propriétaire d'entretenir le bien loué"
            ],
            "steps": [
                "Envoyez d'abord une mise en demeure écrite au propriétaire (obligatoire)",
                "Attendez 15 jours sans réponse, puis saisissez la commune",
                "Demandez un constat officiel d'insalubrité",
                "En cas de refus du propriétaire : TPI pour travaux forcés"
            ],
            "deadline": "Mise en demeure préalable obligatoire avant tout recours (Art. 28)",
            "contacts": [
                "Commune / Service d'Hygiène",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    @Rule(JurisFact(domain='logement', probleme='Caution non rendue'))
    def rule_logement_caution(self):
        self.result = {
            "urgency": "orange",
            "title": "Caution Non Restituée après Départ",
            "rights": [
                "Le propriétaire dispose d'1 mois après état des lieux pour restituer",
                "Sans état des lieux de sortie, la caution est due intégralement",
                "Prescription : 5 ans pour agir en justice"
            ],
            "steps": [
                "Envoyez une mise en demeure recommandée au propriétaire",
                "En cas de refus, saisissez le Tribunal de Première Instance",
                "Réclamez la caution + intérêts si retard injustifié"
            ],
            "deadline": "Mise en demeure recommandée dans le mois suivant le départ",
            "contacts": [
                "Tribunal de Première Instance (TPI) de votre ville"
            ]
        }

    @Rule(JurisFact(domain='logement', contrat_ecrit='Non, accord verbal'))
    def rule_logement_bail_verbal(self):
        self.result = {
            "urgency": "orange",
            "title": "Bail Verbal — Situation Précaire (Art. 4 Loi 67-12)",
            "rights": [
                "Bail verbal reconnu légalement mais difficile à prouver",
                "Durée présumée : 1 an renouvelable",
                "Tous les droits du locataire s'appliquent malgré l'absence de contrat"
            ],
            "steps": [
                "Régularisez la situation avec un contrat écrit dès que possible",
                "Conservez toutes les preuves de paiement (virement, reçus)",
                "En cas de litige, témoins et relevés bancaires serviront de preuves"
            ],
            "deadline": "Aucun délai immédiat, mais régularisez rapidement",
            "contacts": [
                "Notaire ou adoul pour rédiger un contrat de bail",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    # ============================================================
    #  DROIT DE LA FAMILLE — Moudawwana (Loi n° 70-03)
    # ============================================================

    @Rule(JurisFact(domain='famille', probleme='Divorce', accord='Oui'))
    def rule_famille_divorce_amiable(self):
        self.result = {
            "urgency": "green",
            "title": "Divorce par Consentement Mutuel — Mubara'a (Art. 114 Moudawwana)",
            "rights": [
                "Procédure simplifiée et rapide (1 à 3 mois)",
                "Liberté de fixer les modalités de garde, pension et partage",
                "Aucun motif à justifier devant le juge"
            ],
            "steps": [
                "Présentez-vous ensemble au Tribunal de la Famille",
                "Déposez une demande conjointe de divorce",
                "Le juge convoque les deux parties pour vérifier l'accord",
                "Jugement homologué et enregistré à l'état civil"
            ],
            "deadline": "Délai variable : 1 à 3 mois selon le tribunal",
            "contacts": [
                "Section de Justice de la Famille — Tribunal de la Famille",
                "Adoul pour l'enregistrement de l'acte"
            ]
        }

    @Rule(JurisFact(domain='famille', probleme='Divorce', accord='Non'))
    def rule_famille_divorce_contentieux(self):
        self.result = {
            "urgency": "orange",
            "title": "Divorce Contentieux — Chiqaq ou Tatliq (Art. 94-98 Moudawwana)",
            "rights": [
                "Le mari peut exercer le Talaq avec compensation financière (Art. 78)",
                "La femme peut demander le divorce pour préjudice — Tatliq (Art. 98)",
                "Divorce pour discorde — Chiqaq (Art. 94) : ouvert aux deux époux"
            ],
            "steps": [
                "Saisissez le Tribunal de la Famille avec un avocat",
                "Tentative de conciliation obligatoire par le juge",
                "En cas d'échec : jugement fixant garde, pension et Mout'aa",
                "Enregistrement du divorce à l'état civil"
            ],
            "deadline": "Aucun délai de prescription, mais agissez rapidement pour les droits financiers",
            "contacts": [
                "Section de Justice de la Famille — Tribunal de la Famille",
                "Ordre des Avocats de votre barreau"
            ]
        }

    @Rule(JurisFact(domain='famille', probleme='Pension alimentaire', impayee='Plus de 3 mois'))
    def rule_famille_pension_impayee(self):
        self.result = {
            "urgency": "red",
            "title": "Pension Alimentaire Impayée — Plus de 3 Mois (Art. 191 Moudawwana)",
            "rights": [
                "Contrainte par corps contre le débiteur (Art. 191)",
                "Saisie sur salaire ou compte bancaire via ordonnance judiciaire",
                "Récupération rétroactive des arriérés jusqu'à 3 ans"
            ],
            "steps": [
                "Saisissez immédiatement le parquet du Tribunal de la Famille",
                "Demandez une ordonnance de saisie sur salaire",
                "Déposez une plainte pénale pour abandon de famille si nécessaire",
                "Réclamez tous les arriérés + les mois en cours"
            ],
            "deadline": "Arriérés récupérables : 3 ans maximum (prescription)",
            "contacts": [
                "Section de Justice de la Famille — Parquet",
                "Tribunal de la Famille de votre ville"
            ]
        }

    @Rule(JurisFact(domain='famille', probleme='Garde d\'enfants', accord='Non'))
    def rule_famille_garde_litige(self):
        self.result = {
            "urgency": "orange",
            "title": "Garde d'Enfants Contentieuse (Art. 171 Moudawwana)",
            "rights": [
                "Garde (Hadana) attribuée par défaut à la mère jusqu'à 7 ans (garçon) ou mariage (fille)",
                "Le père conserve la tutelle légale (Wilaya) dans tous les cas",
                "Droit de visite et d'hébergement pour le parent non gardien"
            ],
            "steps": [
                "Saisissez le juge des affaires familiales avec un dossier complet",
                "Prouvez votre capacité à assurer l'intérêt supérieur de l'enfant",
                "Toute modification ultérieure nécessite un nouveau jugement"
            ],
            "deadline": "Aucun délai fixe, mais agissez rapidement pour stabiliser la situation",
            "contacts": [
                "Section de Justice de la Famille — Tribunal de la Famille"
            ]
        }

    @Rule(JurisFact(domain='famille', probleme='Héritage / Succession'))
    def rule_famille_heritage(self):
        self.result = {
            "urgency": "green",
            "title": "Héritage et Succession (Art. 325-393 Moudawwana — Fara'id)",
            "rights": [
                "Parts héréditaires fixées par le droit musulman (Fara'id)",
                "Droit à l'acte de notoriété héréditaire (Wassiqa Irathiya)",
                "Possibilité de testament limité au tiers de la succession"
            ],
            "steps": [
                "Obtenez l'acte de décès et le certificat d'hérédité auprès des adoul",
                "Établissez la liste des héritiers et des biens",
                "Saisissez le notaire (adoul) ou le TPI pour partage officiel",
                "En cas de désaccord entre héritiers : TPI pour partage judiciaire"
            ],
            "deadline": "Aucune prescription pour ouvrir la succession, mais agissez tôt pour éviter les conflits",
            "contacts": [
                "Adoul (notaire traditionnel) de votre ville",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    @Rule(JurisFact(domain='famille', type_mariage='Non enregistré'))
    def rule_famille_mariage_non_enregistre(self):
        self.result = {
            "urgency": "red",
            "title": "Mariage Non Enregistré — Action en Reconnaissance Urgente (Art. 16 Moudawwana)",
            "rights": [
                "Reconnaissance judiciaire possible si les deux époux sont vivants",
                "Filiation des enfants protégée si action engagée avant leur majorité",
                "Délai limité : avant le décès d'un des époux"
            ],
            "steps": [
                "Saisissez le Tribunal de la Famille pour reconnaissance de mariage",
                "Fournissez preuves de vie commune (témoins, photos, domicile commun)",
                "Régularisez l'état civil des enfants en parallèle",
                "Agissez avant tout divorce ou décès"
            ],
            "deadline": "URGENT — avant le décès d'un des époux ou la majorité des enfants",
            "contacts": [
                "Section de Justice de la Famille — Tribunal de la Famille",
                "Adoul pour conseil"
            ]
        }

    # ============================================================
    #  DROIT DU CONSOMMATEUR — Loi n° 31-08
    # ============================================================

    @Rule(JurisFact(domain='consommateur', probleme='Achat Internet', delai='Moins de 7 jours'))
    def rule_conso_retractation(self):
        self.result = {
            "urgency": "green",
            "title": "Droit de Rétractation — Vente à Distance (Art. 36 Loi 31-08)",
            "rights": [
                "Rétractation sans justification dans les 7 jours",
                "Remboursement intégral obligatoire sous 15 jours",
                "Le vendeur ne peut imposer aucune pénalité"
            ],
            "steps": [
                "Envoyez une notification écrite de rétractation au vendeur (email ou courrier)",
                "Renvoyez le produit dans son état d'origine",
                "Si pas de remboursement sous 15 jours : saisissez la DPCI"
            ],
            "deadline": "7 jours calendaires à partir de la réception du produit (Art. 36)",
            "contacts": [
                "DPCI — Direction Protection Consommateur : www.mcinet.gov.ma",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    @Rule(JurisFact(domain='consommateur', probleme='Vice caché', delai='7 jours à 2 ans'))
    def rule_conso_vice_cache(self):
        self.result = {
            "urgency": "orange",
            "title": "Vice Caché — Garantie Légale (Art. 549 Code des Obligations et Contrats)",
            "rights": [
                "Garantie légale des vices cachés : 2 ans à partir de la livraison",
                "Choix entre remboursement intégral ou échange du produit",
                "Droit aux dommages et intérêts si vice connu du vendeur"
            ],
            "steps": [
                "Envoyez une mise en demeure écrite au vendeur avec description du vice",
                "Faites établir un constat par un expert si nécessaire",
                "En cas de refus : saisissez la DPCI ou le TPI"
            ],
            "deadline": "2 ans à partir de la date de livraison (Art. 549 DOC)",
            "contacts": [
                "DPCI — Direction Protection Consommateur : www.mcinet.gov.ma",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    @Rule(JurisFact(domain='consommateur', probleme='Vice caché', delai='Plus de 2 ans'))
    def rule_conso_vice_cache_expire(self):
        self.result = {
            "urgency": "orange",
            "title": "Délai de Garantie Légale Expiré (Art. 549 DOC)",
            "rights": [
                "Garantie légale expirée après 2 ans",
                "Recours possible si garantie contractuelle plus longue mentionnée"
            ],
            "steps": [
                "Vérifiez si le contrat ou la facture mentionne une garantie plus longue",
                "En cas de garantie commerciale étendue : réclamez auprès du vendeur",
                "Sinon : aucun recours légal sur le fond"
            ],
            "deadline": "Délai légal de 2 ans dépassé — vérifiez les garanties contractuelles",
            "contacts": [
                "DPCI — Direction Protection Consommateur : www.mcinet.gov.ma"
            ]
        }

    @Rule(JurisFact(domain='consommateur', probleme='Arnaque / Escroquerie'))
    def rule_conso_arnaque(self):
        self.result = {
            "urgency": "red",
            "title": "Arnaque / Escroquerie (Art. 540 Code Pénal Marocain)",
            "rights": [
                "Droit au remboursement via la banque si fraude par carte avérée",
                "Plainte pénale pour escroquerie (Art. 540 CP)",
                "Remboursement bancaire possible par procédure de chargeback"
            ],
            "steps": [
                "Bloquez immédiatement votre carte bancaire si fraude en ligne",
                "Déposez une plainte pénale à la gendarmerie ou la police",
                "Signalez à la DPCI et à votre banque",
                "Conservez toutes les preuves : captures, reçus, échanges"
            ],
            "deadline": "Contestation bancaire : 13 mois maximum | Plainte pénale : 5 ans",
            "contacts": [
                "Police ou Gendarmerie Royale",
                "DPCI : www.mcinet.gov.ma",
                "Votre banque — Service Fraude"
            ]
        }

    @Rule(JurisFact(domain='consommateur', vendeur_type='Particulier'))
    def rule_conso_particulier(self):
        self.result = {
            "urgency": "orange",
            "title": "Litige avec un Particulier — Droit Commun (DOC)",
            "rights": [
                "La Loi 31-08 ne s'applique qu'aux professionnels (Art. 2)",
                "Recours via le Code des Obligations et Contrats (DOC)",
                "Droit aux dommages et intérêts si préjudice prouvé"
            ],
            "steps": [
                "Envoyez une mise en demeure au vendeur particulier",
                "Tentez une médiation amiable",
                "Saisissez le Tribunal de Première Instance (TPI) si échec"
            ],
            "deadline": "Prescription droit commun : 5 ans (Art. 387 DOC)",
            "contacts": [
                "Tribunal de Première Instance (TPI) de votre ville"
            ]
        }

    @Rule(JurisFact(domain='consommateur', montant='Moins de 500 MAD'))
    def rule_conso_petit_montant(self):
        self.result = {
            "urgency": "green",
            "title": "Petit Litige Consommateur — Médiation Recommandée",
            "rights": [
                "Droit à la médiation gratuite avant toute action judiciaire",
                "Droit au remboursement ou échange selon les termes de vente"
            ],
            "steps": [
                "Contactez d'abord le service client du vendeur par écrit",
                "Saisissez la DPCI pour médiation gratuite",
                "Les frais de procédure judiciaire seraient disproportionnés pour ce montant"
            ],
            "deadline": "Agissez dans les 2 ans (prescription droit de la consommation)",
            "contacts": [
                "DPCI — Direction Protection Consommateur : www.mcinet.gov.ma"
            ]
        }

    # ============================================================
    #  DROIT ROUTIER — Loi n° 52-05
    # ============================================================

    @Rule(JurisFact(domain='routier', probleme='PV / Amende', conteste='Non'))
    def rule_routier_pv_non_paye(self):
        self.result = {
            "urgency": "orange",
            "title": "Contestation d'Amende — Ne Payez Pas Encore (Art. 212 Loi 52-05)",
            "rights": [
                "Droit de contester l'amende avant tout paiement",
                "Le paiement vaut reconnaissance définitive de l'infraction",
                "Droit de demander le rapport de verbalisation"
            ],
            "steps": [
                "Ne payez pas l'amende tant que vous souhaitez contester",
                "Déposez un recours au Tribunal de Première Instance dans les 30 jours",
                "Demandez le cliché radar ou le rapport de verbalisation",
                "Préparez vos arguments (erreur de plaque, véhicule vendu, etc.)"
            ],
            "deadline": "30 jours pour contester à partir de la réception du PV (Art. 212)",
            "contacts": [
                "Tribunal de Première Instance (TPI) de votre ville",
                "NARSA : www.narsa.ma"
            ]
        }

    @Rule(JurisFact(domain='routier', probleme='PV / Amende', conteste='Oui'))
    def rule_routier_pv_paye(self):
        self.result = {
            "urgency": "green",
            "title": "Amende Déjà Payée — Recours Limité (Art. 212 Loi 52-05)",
            "rights": [
                "Paiement = reconnaissance de l'infraction (aucun recours sur le fond)",
                "Vérifiez uniquement le nombre de points retirés"
            ],
            "steps": [
                "Vérifiez votre solde de points sur le site NARSA",
                "Si des points ont été retirés à tort, contactez le service des permis",
                "En cas d'erreur administrative, recours auprès du Ministère du Transport"
            ],
            "deadline": "Recours administratif : 60 jours après notification",
            "contacts": [
                "NARSA : www.narsa.ma",
                "Ministère du Transport : www.mtpnet.gov.ma"
            ]
        }

    @Rule(JurisFact(domain='routier', points='0 point'))
    def rule_routier_permis_annule(self):
        self.result = {
            "urgency": "red",
            "title": "Permis Annulé — Solde de Points Nul (Art. 177 Loi 52-05)",
            "rights": [
                "Droit au recours administratif auprès du Ministère du Transport",
                "Possibilité de référé-suspension si urgence professionnelle prouvée"
            ],
            "steps": [
                "Remettez votre permis à la préfecture ou la gendarmerie",
                "Attendez le délai légal avant de repasser l'examen",
                "Passez une visite médicale + tests psychotechniques",
                "Repassez le code puis la conduite (examen complet)"
            ],
            "deadline": "Recours administratif : 60 jours après réception de la notification",
            "contacts": [
                "NARSA : www.narsa.ma",
                "Préfecture ou Gendarmerie Royale"
            ]
        }

    @Rule(JurisFact(domain='routier', alcoolemie='Oui'))
    def rule_routier_alcoolemie(self):
        self.result = {
            "urgency": "red",
            "title": "Alcoolémie Constatée — Délit Pénal (Art. 178 Loi 52-05)",
            "rights": [
                "Droit à un avocat dès la garde à vue",
                "Droit de contester le résultat de l'alcootest (contre-expertise)"
            ],
            "steps": [
                "Contactez un avocat spécialisé en droit routier immédiatement",
                "Demandez une contre-expertise si vous contestez le taux",
                "Ne faites aucune déclaration sans votre avocat",
                "Préparez-vous à une convocation au tribunal correctionnel"
            ],
            "deadline": "Taux > 0,8 g/l = délit pénal avec retrait immédiat du permis",
            "contacts": [
                "Ordre des Avocats de votre barreau",
                "Tribunal de Première Instance (TPI)"
            ]
        }

    @Rule(JurisFact(domain='routier', probleme='Accident', blesses='Oui'))
    def rule_routier_accident_blesses(self):
        self.result = {
            "urgency": "red",
            "title": "Accident avec Blessés — Responsabilité Pénale et Civile (Art. 237 Loi 52-05)",
            "rights": [
                "Prise en charge médicale par l'assurance automobile",
                "Droit à la défense pénale et civile",
                "Recours en indemnisation si vous êtes victime"
            ],
            "steps": [
                "Appelez le 15 (SAMU) et le 19 (Police) immédiatement",
                "Déclarez l'accident à votre assurance sous 5 jours ouvrables",
                "Remplissez un constat amiable si possible",
                "Consultez un avocat si mise en cause pénale"
            ],
            "deadline": "Déclaration assurance : 5 jours | Prescription accidents : 5 ans",
            "contacts": [
                "SAMU : 15 | Police : 19 | Gendarmerie : 177",
                "Votre compagnie d'assurance automobile"
            ]
        }

    @Rule(JurisFact(domain='routier', probleme='Retrait de permis'))
    def rule_routier_retrait_permis(self):
        self.result = {
            "urgency": "orange",
            "title": "Retrait ou Suspension de Permis (Art. 180 Loi 52-05)",
            "rights": [
                "Stage de récupération de points si solde entre 1 et 10 points (Art. 180)",
                "Recours administratif au Ministère du Transport dans les 60 jours",
                "Référé-suspension possible si permis indispensable à l'activité professionnelle"
            ],
            "steps": [
                "Vérifiez votre solde de points sur NARSA (www.narsa.ma)",
                "Inscrivez-vous à un stage de récupération de points agréé",
                "Si suspension abusive : recours administratif dans les 60 jours",
                "Consultez un avocat pour un référé-suspension si urgence professionnelle"
            ],
            "deadline": "Recours administratif : 60 jours après réception de la décision",
            "contacts": [
                "NARSA : www.narsa.ma",
                "Ministère du Transport : www.mtpnet.gov.ma"
            ]
        }