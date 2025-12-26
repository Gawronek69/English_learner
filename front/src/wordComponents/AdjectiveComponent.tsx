import { useEffect, useState } from 'react';
import type { BaseWord } from '../utils/WordInterfaces';
import { fetchWordsFromServer } from '../utils/WordGetter.tsx';

import type {AdjMeta, Degree} from "../utils/WordInterfaces";
import type {StateType} from "../AppState.tsx";

type Props = {
    onWordSelect: (word: BaseWord, meta: AdjMeta, state: StateType) => void;
};

export function AdjectiveComponent({ onWordSelect }: Props) {

    const startingMeta: AdjMeta = {
        degree: 'positive',
    }

    const [words, setWords] = useState<BaseWord[]>([]);
    const [selectedWord, setSelectedWord] = useState<BaseWord | null>(null);
    const [meta, setmeta] = useState<AdjMeta>(startingMeta);

    useEffect(() => {
        fetchWordsFromServer('adj').then(setWords);
    }, []);

    const handleConfirm = (state: StateType) => {
        if (selectedWord) {
            onWordSelect(selectedWord, meta, state);
            setSelectedWord(null);
            setmeta(startingMeta);
        }
    };

    return (
        <div className="word-component">
            <h3 className="category-title">Wybierz Przymiotnik</h3>

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
                            Stopień:
                            <select
                                value={meta.degree}
                                onChange={(e) => setmeta({degree : e.target.value as Degree})}
                            >
                                <option value="singular">Równy</option>
                                <option value="plural">Wyższy</option>
                                <option value="plural">Najwyższy</option>
                            </select>
                        </label>
                    </div>
                    <div className="buttons">
                        <button className="btn-confirm" onClick={() => {handleConfirm('NOUN')}}>
                            Przejdź do Rzeczownika
                        </button>
                        <button className="btn-confirm" onClick={() => {handleConfirm('CONJ')}}>
                            Przejdź do Spójnika - łączenie rzeczowników
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