import React, { useEffect, useState } from 'react';

const DomainSelector = ({ onSelect }) => {
    const [domains, setDomains] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8000/api/domains')
            .then(res => res.json())
            .then(setDomains);
    }, []);

    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {domains.map((d) => (
                <button
                    key={d.id}
                    onClick={() => onSelect(d.id)}
                    className="group relative bg-gray-50 border border-gray-200 p-8 rounded-2xl text-left hover:border-green-DEFAULT hover:bg-green-light/30 transition-all duration-300 overflow-hidden shadow-sm hover:shadow-md"
                >
                    <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                        <span className="text-6xl">{d.icon}</span>
                    </div>
                    <div className="relative z-10 space-y-4">
                        <span className="text-4xl block mb-2">{d.icon}</span>
                        <h3 className="text-xl font-serif text-green-dark font-semibold">{d.label}</h3>
                        <p className="text-sm text-gray-500">Cliquez pour démarrer l'assistance personnalisée.</p>
                    </div>
                </button>
            ))}
            <div className="bg-gray-50 border border-dashed border-gray-300 p-8 rounded-2xl flex flex-col justify-center items-center text-center">
                <p className="text-sm text-gray-500 italic">Besoin d'autre chose ?</p>
                <button onClick={() => onSelect(null)} className="text-green-DEFAULT font-bold mt-2 hover:underline">Poser une question libre →</button>
            </div>
        </div>
    );
};

export default DomainSelector;
