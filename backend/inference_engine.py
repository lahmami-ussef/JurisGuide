from experta import KnowledgeEngine, Rule, Fact, MATCH, AS
from typing import Dict, Any

class JurisFact(Fact):
    """Structure de fait pour JurisGuide."""
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

    # --- DROIT DU TRAVAIL ---
    @Rule(JurisFact(domain='travail', contrat='CDI', anciennete='> 2 ans', probleme='Licenciement', notification='SMS'))
    def rule_travail_licenciement_sms(self):
        self.result = {
            "urgency": "red",
            "title": "Licenciement Verbal/SMS (Irrégulier)",
            "rights": [
                "Indemnité de licenciement légale ou conventionnelle",
                "Indemnité compensatrice de préavis",
                "Dommages et intérêts pour licenciement sans cause réelle et sérieuse"
            ],
            "steps": [
                "Ne pas signer de démission",
                "Envoyer une mise en demeure par LRAR pour réclamer la lettre officielle",
                "Saisir le Conseil de Prud'hommes en référé",
                "Contacter l'Inspection du Travail"
            ],
            "deadline": "12 mois pour contester la rupture du contrat",
            "letter_type": "contestation_licenciement_sms",
            "contacts": ["Inspection du Travail : 08 06 00 01 26", "Conseil de Prud'hommes"]
        }

    @Rule(JurisFact(domain='travail', probleme='Harcèlement', preuve='Oui'))
    def rule_travail_harcelement(self):
        self.result = {
            "urgency": "red",
            "title": "Harcèlement Moral au Travail",
            "rights": [
                "Protection contre les mesures de rétorsion",
                "Droit de retrait si danger imminent",
                "Résiliation judiciaire du contrat aux torts de l'employeur"
            ],
            "steps": [
                "Alerter le CSE (Comité Social et Économique)",
                "Consulter la médecine du travail",
                "Conserver toutes les preuves (emails, témoignages)",
                "Déposer plainte au pénal"
            ],
            "deadline": "5 ans pour agir au civil, 6 ans au pénal",
            "letter_type": "signalement_harcelement",
            "contacts": ["Médecine du travail", "Défenseur des Droits : 09 69 39 00 00"]
        }

    # --- DROIT DU LOGEMENT ---
    @Rule(JurisFact(domain='logement', probleme='Expulsion', commandement_payer='Oui'))
    def rule_logement_expulsion(self):
        self.result = {
            "urgency": "red",
            "title": "Procédure d'Expulsion Locative",
            "rights": [
                "Droit au maintien dans les lieux pendant la trêve hivernale (1er nov - 31 mars)",
                "Droit de solliciter des délais de paiement devant le juge"
            ],
            "steps": [
                "Contacter l'ADIL immédiatement",
                "Saisir la commission de surendettement si nécessaire",
                "Déposer un dossier DALO (Droit Au Logement Opposable)",
                "Se présenter à l'audience du tribunal"
            ],
            "deadline": "2 mois après le commandement de payer pour régulariser",
            "letter_type": "demande_delai_paiement",
            "contacts": ["ADIL : 0 805 160 075", "Fondation Abbé Pierre : 0 810 001 505"]
        }

    @Rule(JurisFact(domain='logement', probleme='Indécence', proprietaire_alerte='Oui'))
    def rule_logement_insalubrite(self):
        self.result = {
            "urgency": "orange",
            "title": "Logement Non Décent / Insalubre",
            "rights": [
                "Suspension du paiement des loyers (uniquement sur décision judiciaire)",
                "Réduction de loyer",
                "Relogement aux frais du propriétaire"
            ],
            "steps": [
                "Demander un diagnostic de décence à la CAF",
                "Saisir le service d'hygiène de la mairie (SCHS)",
                "Mettre en demeure le propriétaire d'effectuer les travaux",
                "Saisir la CDC (Commission Départementale de Conciliation)"
            ],
            "deadline": "Pas de délai spécifique, mais agir vite avant dégradation de la santé",
            "letter_type": "mise_en_demeure_travaux",
            "contacts": ["CAF", "Mairie (Service Hygiène)"]
        }

    # --- DROIT DE LA FAMILLE ---
    @Rule(JurisFact(domain='famille', probleme='Divorce', accord='Oui'))
    def rule_famille_divorce_amiable(self):
        self.result = {
            "urgency": "green",
            "title": "Divorce par Consentement Mutuel (Extra-judiciaire)",
            "rights": [
                "Procédure rapide sans passage devant le juge",
                "Liberté de fixer les modalités de garde et de pension"
            ],
            "steps": [
                "Chaque conjoint doit avoir son propre avocat",
                "Rédaction d'une convention de divorce",
                "Délai de réflexion de 15 jours après réception de la convention",
                "Enregistrement chez le notaire"
            ],
            "deadline": "Délai de réflexion obligatoire de 15 jours",
            "letter_type": "demande_divorce_amiable",
            "contacts": ["Ordre des Avocats", "Notaire"]
        }

    @Rule(JurisFact(domain='famille', probleme='Pension', impayee='> 2 mois'))
    def rule_famille_pension_impayee(self):
        self.result = {
            "urgency": "red",
            "title": "Pension Alimentaire Impayée",
            "rights": [
                "Recouvrement forcé via l'ARIPA (CAF)",
                "Plainte pour abandon de famille"
            ],
            "steps": [
                "Contacter l'ARIPA (CAF) pour l'intermédiation financière",
                "Demander à un huissier de justice un paiement direct",
                "Déposer plainte au commissariat"
            ],
            "deadline": "Arriérés récupérables sur 5 ans maximum",
            "letter_type": "mise_en_demeure_pension",
            "contacts": ["ARIPA (CAF) : 3238", "Huissier de Justice"]
        }

    # --- DROIT DU CONSOMMATEUR ---
    @Rule(JurisFact(domain='consommateur', probleme='Achat Internet', delai='< 14 jours'))
    def rule_conso_retractation(self):
        self.result = {
            "urgency": "green",
            "title": "Droit de Rétractation (Achat en ligne)",
            "rights": [
                "Remboursement intégral sous 14 jours",
                "Aucune justification nécessaire"
            ],
            "steps": [
                "Envoyer le formulaire de rétractation (par email ou courrier)",
                "Renvoyer le produit à vos frais (sauf mention contraire)",
                "Suivre le remboursement sur votre compte"
            ],
            "deadline": "14 jours calendaires à partir de la réception",
            "letter_type": "retractation_achat_internet",
            "contacts": ["DGCCRF : 0809 540 550", "UFC-Que Choisir"]
        }

    @Rule(JurisFact(domain='consommateur', probleme='Arnaque', montant='> 1000€'))
    def rule_conso_arnaque(self):
        self.result = {
            "urgency": "red",
            "title": "Escroquerie / Arnaque de montant important",
            "rights": [
                "Remboursement par la banque si phishing avéré sans négligence grave",
                "Droit au dépôt de plainte"
            ],
            "steps": [
                "Faire opposition sur la carte/virement immédiatement",
                "Signaler sur la plateforme PHAROS",
                "Déposer plainte en ligne (THESEE) ou au commissariat",
                "Demander le 'chargeback' à votre banque"
            ],
            "deadline": "13 mois pour contester un paiement frauduleux par carte",
            "letter_type": "contestation_operation_bancaire",
            "contacts": ["Info Escroqueries : 0 805 805 817", "Banque (Service Fraude)"]
        }

    # --- DROIT ROUTIER ---
    @Rule(JurisFact(domain='routier', probleme='PV', conteste='Non'))
    def rule_routier_pv_excessif(self):
        self.result = {
            "urgency": "orange",
            "title": "Contestation d'Amende Forfaitaire",
            "rights": [
                "Droit de contester avant de payer",
                "Droit de demander la photo du radar"
            ],
            "steps": [
                "Ne pas payer l'amende (le paiement vaut reconnaissance)",
                "Consigner le montant si nécessaire",
                "Effectuer la contestation sur le site de l'ANTAI",
                "Demander le cliché de verbalisation"
            ],
            "deadline": "45 jours pour une amende forfaitaire (30 jours si radar)",
            "letter_type": "contestation_pv_radar",
            "contacts": ["ANTAI (antai.gouv.fr)", "Officier du Ministère Public (OMP)"]
        }

    @Rule(JurisFact(domain='routier', probleme='Permis', points='0'))
    def rule_routier_suspension(self):
        self.result = {
            "urgency": "red",
            "title": "Invalidation du Permis (Solde de points nul)",
            "rights": [
                "Droit au recours gracieux devant le Ministre de l'Intérieur",
                "Possibilité de référé-suspension si urgence professionnelle"
            ],
            "steps": [
                "Remettre le permis à la préfecture sous 10 jours après réception de la lettre 48SI",
                "Attendre 6 mois pour repasser le code",
                "Passer une visite médicale et des tests psychotechniques",
                "Contacter un avocat expert en droit routier"
            ],
            "deadline": "2 mois pour contester la décision 48SI",
            "letter_type": "recours_gracieux_permis",
            "contacts": ["Préfecture", "Service Fichier National des Permis de Conduire"]
        }
