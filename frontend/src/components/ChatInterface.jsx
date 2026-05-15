import React, { useState, useEffect, useRef } from 'react';
import useChat from '../hooks/useChat';

const ChatInterface = ({ session, onFinish, onReset }) => {
    const { messages, loading, sendMessage, currentOptions } = useChat(session);
    const [inputValue, setInputValue] = useState('');
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, loading]);

    const handleSend = (text) => {
        const messageText = text || inputValue;
        if (!messageText.trim()) return;

        sendMessage(messageText, (result) => {
            if (result) onFinish(result);
        });
        setInputValue('');
    };

    return (
        <div className="bg-[#14141c] border border-[#c9a84c]/20 rounded-2xl overflow-hidden flex flex-col h-[70vh] shadow-2xl">
            {/* Messages */}
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
                {messages.map((msg, idx) => (
                    <div
                        key={idx}
                        className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in slide-in-from-bottom-2 duration-300`}
                    >
                        <div className={`max-w-[80%] p-4 rounded-2xl ${msg.role === 'user'
                                ? 'bg-[#c9a84c] text-black font-medium rounded-tr-none'
                                : 'bg-[#1a1a25] border border-[#c9a84c]/10 rounded-tl-none'
                            }`}>
                            {msg.text}
                        </div>
                    </div>
                ))}
                {loading && (
                    <div className="flex justify-start">
                        <div className="bg-[#1a1a25] p-4 rounded-2xl rounded-tl-none flex gap-1 items-center">
                            <span className="w-1.5 h-1.5 bg-[#c9a84c] rounded-full animate-bounce"></span>
                            <span className="w-1.5 h-1.5 bg-[#c9a84c] rounded-full animate-bounce delay-100"></span>
                            <span className="w-1.5 h-1.5 bg-[#c9a84c] rounded-full animate-bounce delay-200"></span>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input / Options */}
            <div className="p-6 bg-[#0a0a0f] border-t border-[#c9a84c]/10 space-y-4">
                {currentOptions && currentOptions.length > 0 && (
                    <div className="flex flex-wrap gap-2">
                        {currentOptions.map((opt, i) => (
                            <button
                                key={i}
                                onClick={() => handleSend(opt)}
                                className="px-4 py-2 bg-transparent border border-[#c9a84c] text-[#c9a84c] rounded-full text-sm hover:bg-[#c9a84c] hover:text-black transition-all"
                            >
                                {opt}
                            </button>
                        ))}
                    </div>
                )}
                <div className="flex gap-3">
                    <input
                        type="text"
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                        placeholder="Répondez ici..."
                        className="flex-1 bg-[#14141c] border border-[#c9a84c]/20 rounded-xl px-4 py-3 focus:outline-none focus:border-[#c9a84c] transition-colors"
                    />
                    <button
                        onClick={() => handleSend()}
                        className="bg-[#c9a84c] text-black p-3 rounded-xl hover:bg-[#b09341] transition-colors"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ChatInterface;
