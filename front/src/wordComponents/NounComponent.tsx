import { useEffect, useState } from 'react';
import type { BaseWord } from '../utils/WordInterfaces';
import { fetchWordsFromServer } from '../utils/WordGetter.tsx';
import type { NounMeta } from "../utils/WordInterfaces";
import type { StateType } from "../AppState.tsx";

type Props = {
    onWordSelect: (word: BaseWord, meta: NounMeta, state: StateType) => void;
};

export function NounComponent({ onWordSelect }: Props) {
    const [words, setWords] = useState<BaseWord[]>([]);
    const [selectedWord, setSelectedWord] = useState<BaseWord | null>(null);
    const [count, setCount] = useState<'singular' | 'plural'>('singular');

    useEffect(() => {
        fetchWordsFromServer('noun').then(setWords);
    }, []);

    const handleConfirm = (state: StateType) => {
        if (selectedWord) {
            onWordSelect(selectedWord, { count }, state);
            setSelectedWord(null);
            setCount('singular');
        }
    };

    return (
        <div className="word-component">
            <h3 className="category-title">Wybierz Rzeczownik</h3>

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

                    <div className="form-group">
                        <label>
                            Liczba:
                            <select
                                value={count}
                                onChange={(e) => setCount(e.target.value as 'singular' | 'plural')}
                            >
                                <option value="singular">Pojedyncza</option>
                                <option value="plural">Mnoga</option>
                            </select>
                        </label>
                    </div>

                    <div className="buttons">
                        <button className="btn-confirm" onClick={() => {handleConfirm('VERB')}}>
                            Przejdź do Czasownika
                        </button>
                        <button className="btn-confirm" onClick={() => {handleConfirm('PREP')}}>
                            Przejdź do Przyimka (Miejsce)
                        </button>
                        <button className="btn-confirm" onClick={() => {handleConfirm('CONJ')}}>
                            Przejdź do Spójnika (Łączenie)
                        </button>
                        <button className="btn-confirm" onClick={() => {handleConfirm('END')}}>
                            Koniec Zdania
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}