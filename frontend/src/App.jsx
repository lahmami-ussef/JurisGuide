import React, { useState } from 'react';
import DomainSelector from './components/DomainSelector';
import ChatInterface from './components/ChatInterface';
import ResultCard from './components/ResultCard';

const App = () => {
  const [session, setSession] = useState(null);
  const [result, setResult] = useState(null);

  const [isLoadingSession, setIsLoadingSession] = useState(false);

  const resetApp = () => {
    setSession(null);
    setResult(null);
  };

  const handleDomainSelect = async (domainId) => {
    setIsLoadingSession(true);
    try {
      const res = await fetch('http://localhost:8000/api/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ domain: domainId })
      });
      const data = await res.json();
      setSession(data);
    } catch (err) {
      console.error("Erreur lors du démarrage de la session:", err);
    } finally {
      setIsLoadingSession(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#050505] text-white p-4 font-sans flex flex-col items-center">
      <header className="w-full max-w-4xl py-6 flex items-center justify-between border-b border-[#c9a84c]/20 mb-8">
        <h1 className="text-3xl font-serif text-[#c9a84c] tracking-wider">JURISGUIDE</h1>
        {session && (
          <button onClick={resetApp} className="text-sm opacity-60 hover:text-[#c9a84c] transition-colors">
            Nouvelle consultation
          </button>
        )}
      </header>

      <main className="w-full max-w-4xl flex-grow flex flex-col">
        {!session && !result && (
          isLoadingSession ? (
            <div className="flex justify-center items-center h-64">
              <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#c9a84c]"></div>
            </div>
          ) : (
            <DomainSelector onSelect={handleDomainSelect} />
          )
        )}
        {session && !result && <ChatInterface session={session} onFinish={setResult} />}
        {result && <ResultCard result={result} onReset={resetApp} />}
      </main>
    </div>
  );
};

export default App;
