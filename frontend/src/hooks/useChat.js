import { useState, useEffect } from 'react';

const useChat = (initialSession) => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(initialSession?.session_id);
  const [currentOptions, setCurrentOptions] = useState(initialSession?.options || []);

  useEffect(() => {
    if (initialSession) {
      setMessages([
        { role: 'bot', text: initialSession.message }
      ]);
    }
  }, [initialSession]);

  const sendMessage = async (text, callback) => {
    if (!text || loading) return;

    // Ajouter le message utilisateur
    const userMsg = { role: 'user', text };
    setMessages(prev => [...prev, userMsg]);
    setLoading(true);
    setCurrentOptions([]);

    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          message: text
        })
      });

      const data = await response.json();
      
      // Ajouter la réponse du bot
      setMessages(prev => [...prev, { role: 'bot', text: data.message }]);
      setCurrentOptions(data.options || []);

      if (data.is_final && data.result) {
        // Un petit délai pour l'effet de lecture
        setTimeout(() => {
          callback(data.result);
          setLoading(false);
        }, 1500);
      } else {
        setLoading(false);
      }

    } catch (error) {
      console.error("Erreur API Chat:", error);
      setMessages(prev => [...prev, { role: 'bot', text: "Désolé, une erreur technique est survenue. Veuillez réessayer." }]);
      setLoading(false);
    }
  };

  return {
    messages,
    loading,
    sendMessage,
    currentOptions
  };
};

export default useChat;
