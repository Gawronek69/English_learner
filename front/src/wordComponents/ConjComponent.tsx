import { useEffect, useState } from 'react';
import type { BaseWord } from '../utils/WordInterfaces';
import { fetchWordsFromServer } from '../utils/WordGetter.tsx';
import type {StateType} from "../AppState.tsx";


type Props = {
    onWordSelect: (word: BaseWord, meta: null, state: StateType) => void;
};

export function ConjComponent({ onWordSelect }: Props) {
    const [words, setWords] = useState<BaseWord[]>([]);
    const [selectedWord, setSelectedWord] = useState<BaseWord | null>(null);

    useEffect(() => {
        fetchWordsFromServer('conj').then(setWords);
    }, []);

    const handleConfirm = (state: StateType) => {
        if (selectedWord) {
            onWordSelect(selectedWord,  null, state);
            setSelectedWord(null);
        }
    };

    return (
        <div className="word-component">
            <h3 className="category-title">Wybierz Spójnik</h3>

            <div className="scroll-container">
                <div className="words-grid">
                    {words.map((item) => (
                        <button
                            key={item.word}
                            className={`word-card noun-card ${selectedWord?.word === item.word ? 'selected' : ''}`}
                            onClick={() => setSelectedWord(item)}
                        >
                            {item.word}
                        </button>
                    ))}
                </div>
            </div>

            {selectedWord && (
                <div className="options-panel">
                    <h4>Konfiguracja: {selectedWord.word}</h4>

                    <div className="buttons">
                        <button className="btn-confirm" onClick={() => {handleConfirm('NOUN')}}>
                            Przejdź do Rzeczownika
                        </button>
                        <button className="btn-confirm" onClick={() => {handleConfirm('ADJ')}}>
                            Przejdź do Przymiotnika
                        </button>
                        <button className="btn-confirm" onClick={() => {handleConfirm('VERB')}}>
                            Przejdź do Czasownika
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}