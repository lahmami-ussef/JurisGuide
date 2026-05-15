import React, { useState } from 'react';
import LetterModal from './LetterModal';
const ResultCard = ({ result, onReset }) => {
  const [showLetter, setShowLetter] = useState(false);
  const urgencyColors = {
    red: 'bg-red-500/20 text-red-500 border-red-500/50',
    orange: 'bg-orange-500/20 text-orange-500 border-orange-500/50',
    green: 'bg-green-500/20 text-green-500 border-green-500/50'
  };
  const urgencyLabels = {
    red: 'URGENCE CRITIQUE',
    orange: 'CONSEILLÉ D\'AGIR VITE',
    green: 'SITUATION STABLE'
  };
  if (!result) return null;
  return (
    <div className="bg-[#14141c] border border-[#c9a84c]/30 rounded-3xl p-8 space-y-10 shadow-[0_0_50px_-12px_rgba(201,168,76,0.3)] animate-in zoom-in-95 duration-500">
      {/* Header Result */}
      <div className="flex flex-col md:flex-row justify-between items-start gap-6 border-b border-[#c9a84c]/10 pb-8">
        <div className="space-y-2">
          <span className={`px-3 py-1 rounded-full text-xs font-bold border ${urgencyColors[result.urgency] || urgencyColors.orange}`}>
            {urgencyLabels[result.urgency] || urgencyLabels.orange}
          </span>
          <h2 className="text-4xl font-serif text-[#c9a84c] leading-tight">{result.title || "Analyse de votre situation"}</h2>
        </div>
        <button 
          onClick={onReset}
          className="px-4 py-2 rounded-xl border border-[#c9a84c]/20 text-sm opacity-60 hover:opacity-100 hover:border-[#c9a84c] hover:text-[#c9a84c] transition-all flex items-center gap-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Recommencer
        </button>
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
        {/* Colonne Gauche (2/3) : Droits et Démarches */}
        <div className="lg:col-span-2 space-y-12">
          <section className="space-y-6">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-[#c9a84c]/10 rounded-lg flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-[#c9a84c]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-2xl font-serif text-[#c9a84c]">Vos Droits</h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {result.rights?.map((right, i) => (
                <div key={i} className="bg-[#1a1a25] p-4 rounded-xl border border-[#c9a84c]/5 flex gap-4 items-start">
                  <span className="text-[#c9a84c] mt-1 text-lg">✦</span>
                  <p className="text-sm leading-relaxed opacity-90">{right}</p>
                </div>
              ))}
            </div>
          </section>
          <section className="space-y-6">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-[#c9a84c]/10 rounded-lg flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-[#c9a84c]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 002-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h3 className="text-2xl font-serif text-[#c9a84c]">Démarches à suivre</h3>
            </div>
            <div className="space-y-4">
              {result.steps?.map((step, i) => (
                <div key={i} className="flex gap-6 p-5 bg-[#0a0a0f] rounded-2xl border border-[#c9a84c]/10 hover:border-[#c9a84c]/30 transition-all group">
                  <div className="w-10 h-10 rounded-full bg-[#c9a84c] flex items-center justify-center text-black font-bold shrink-0 shadow-lg shadow-[#c9a84c]/20">
                    {i + 1}
                  </div>
                  <p className="text-base opacity-80 group-hover:opacity-100 transition-opacity self-center">{step}</p>
                </div>
              ))}
            </div>
          </section>
        </div>
        {/* Colonne Droite (1/3) : Délais, Contacts et Documents */}
        <div className="space-y-8">
          {/* Section Délais Légaux */}
          <div className="bg-[#0a0a0f] border border-[#c9a84c]/20 rounded-2xl p-6 space-y-4">
            <div className="flex items-center gap-3 opacity-60">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <h4 className="text-xs uppercase tracking-widest font-bold">Délais Légaux</h4>
            </div>
            <p className="text-lg font-medium text-cream">{result.deadline || "À vérifier selon juridiction"}</p>
          </div>
          {/* Section Organismes */}
          <div className="bg-[#0a0a0f] border border-[#c9a84c]/20 rounded-2xl p-6 space-y-4">
            <div className="flex items-center gap-3 opacity-60">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
              <h4 className="text-xs uppercase tracking-widest font-bold">Organismes Utiles</h4>
            </div>
            <div className="flex flex-col gap-3">
              {result.contacts?.map((contact, i) => (
                <div key={i} className="flex items-center gap-2 text-sm bg-[#1a1a25] p-3 rounded-lg border border-[#c9a84c]/5 hover:bg-[#c9a84c]/10 transition-colors cursor-default">
                  <span className="w-1.5 h-1.5 bg-[#c9a84c] rounded-full"></span>
                  {contact}
                </div>
              ))}
            </div>
          </div>
          {/* Section Documents */}
          <div className="bg-[#c9a84c]/10 border border-[#c9a84c] rounded-2xl p-6 space-y-4">
            <div className="flex items-center gap-3 text-[#c9a84c]">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
              <h4 className="text-xs uppercase tracking-widest font-bold">Documents Disponibles</h4>
            </div>
            
            {result.letter_type ? (
              <div className="space-y-4">
                <p className="text-xs opacity-70">Une lettre type a été générée en fonction de votre situation spécifique.</p>
                <button 
                  onClick={() => setShowLetter(true)}
                  className="w-full bg-[#c9a84c] text-black font-bold py-4 rounded-xl hover:bg-[#b09341] transition-all flex items-center justify-center gap-3 shadow-lg shadow-[#c9a84c]/20"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  Voir la lettre type
                </button>
              </div>
            ) : (
              <p className="text-xs opacity-40 italic">Aucun document spécifique pour cette situation.</p>
            )}
          </div>
          
          <div className="p-4 bg-blue-500/5 border border-blue-500/20 rounded-xl flex gap-4">
             <div className="shrink-0 text-blue-400 text-xl">ℹ️</div>
             <p className="text-[10px] text-blue-400/80 leading-relaxed uppercase tracking-tighter">
               JurisGuide est un assistant automatisé. Ne négligez jamais un avis professionnel.
             </p>
          </div>
        </div>
      </div>
      {showLetter && (
        <LetterModal 
          letterType={result.letter_type} 
          onClose={() => setShowLetter(false)} 
        />
      )}
    </div>
  );
};
export default ResultCard;
