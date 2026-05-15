import React, { useState, useEffect } from 'react';

const LetterModal = ({ letterType, onClose }) => {
  const [content, setContent] = useState('');
  const [copied, setCopied] = useState(false);

  // Simulation de récupération de la lettre depuis une constante (ou API si nécessaire)
  // Pour la démo, on utilise une structure simple
  const TEMPLATES = {
    "contestation_licenciement_sms": `
[Votre Nom]
[Votre Adresse]

À l'attention de la Direction de [Nom Entreprise]
[Adresse Entreprise]

Fait à [Ville], le [Date du jour]

Objet : Contestation de la rupture de mon contrat de travail

Madame, Monsieur,

J'accuse réception de votre message (SMS) reçu le [Date] m'informant de mon licenciement.

Par la présente, je tiens à vous informer que je conteste formellement la régularité de cette procédure. En effet, l'article L1232-6 du Code du travail impose la notification d'un licenciement par lettre recommandée avec accusé de réception.

À ce jour, je n'ai reçu aucune lettre officielle, ce qui rend mon licenciement privé de cause réelle et sérieuse.

Je reste à votre disposition pour reprendre mon poste de travail immédiatement, à défaut de quoi je me verrai contraint de saisir le Conseil de Prud'hommes compétent.

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

[Signature]
    `,
    "mise_en_demeure_travaux": `
[Votre Nom]
[Votre Adresse]

À l'attention de Monsieur/Madame [Nom du Propriétaire]
[Adresse du Propriétaire]

Fait à [Ville], le [Date du jour]

Objet : Mise en demeure - Travaux de mise en décence

Madame, Monsieur,

Je vous informe par la présente des désordres constatés dans le logement que je vous loue au [Adresse du logement] : [Liste des désordres].

En vertu de l'article 6 de la loi n°89-462 du 6 juillet 1989, le bailleur est tenu de remettre au locataire un logement décent ne laissant pas apparaître de risques manifestes pouvant porter atteinte à la sécurité physique ou à la santé.

Je vous mets en demeure d'effectuer les travaux nécessaires sous un délai de 8 jours à réception de la présente. À défaut de réponse, je saisirai la Commission Départementale de Conciliation.

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

[Signature]
    `,
    "retractation_achat_internet": `
[Votre Nom]
[Votre Adresse]

À l'attention du Service Client de [Nom du Vendeur]
[Adresse du Vendeur]

Fait à [Ville], le [Date du jour]

Objet : Exercice du droit de rétractation

Madame, Monsieur,

Le [Date de la commande], j'ai commandé sur votre site internet le produit suivant : [Nom du produit], reçu le [Date de réception].

Conformément à l'article L221-18 du Code de la consommation, je vous informe que je souhaite exercer mon droit de rétractation pour cette commande.

Je vous retournerai le produit sous 14 jours, dans son emballage d'origine. Je vous prie de me rembourser la somme de [Montant] € correspondant au prix d'achat, frais de livraison inclus, dans les meilleurs délais.

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

[Signature]
    `
  };

  useEffect(() => {
    setContent(TEMPLATES[letterType] || "Modèle non trouvé.");
  }, [letterType]);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const downloadTxt = () => {
    const element = document.createElement("a");
    const file = new Blob([content], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);
    element.download = `jurisguide_lettre_${letterType}.txt`;
    document.body.appendChild(element);
    element.click();
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-gray-900/50 backdrop-blur-sm animate-in fade-in duration-300">
      <div className="bg-white border border-gray-200 rounded-3xl w-full max-w-3xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in zoom-in-95 duration-300">
        {/* Header */}
        <div className="p-6 border-b border-gray-200 flex justify-between items-center bg-gray-50">
          <h3 className="text-xl font-serif text-green-dark font-bold">Votre Lettre Type</h3>
          <button onClick={onClose} className="p-2 hover:bg-gray-200 rounded-full transition-colors text-gray-500">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-8 bg-white">
          <pre className="font-sans text-sm leading-relaxed whitespace-pre-wrap bg-gray-50 p-8 rounded-xl border border-gray-200 text-gray-800">
            {content}
          </pre>
        </div>

        {/* Footer Actions */}
        <div className="p-6 bg-gray-50 border-t border-gray-200 flex flex-col sm:flex-row gap-4">
          <button 
            onClick={copyToClipboard}
            className="flex-1 py-3 px-6 bg-white border border-green-DEFAULT text-green-DEFAULT font-bold rounded-xl hover:bg-green-DEFAULT hover:text-white transition-all flex items-center justify-center gap-2 shadow-sm"
          >
            {copied ? 'Copié !' : 'Copier dans le presse-papier'}
          </button>
          <button 
            onClick={downloadTxt}
            className="flex-1 py-3 px-6 bg-green-DEFAULT text-white font-bold rounded-xl hover:bg-green-dark transition-all flex items-center justify-center gap-2 shadow-md shadow-green-DEFAULT/20"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            Télécharger (.txt)
          </button>
        </div>
      </div>
    </div>
  );
};

export default LetterModal;
