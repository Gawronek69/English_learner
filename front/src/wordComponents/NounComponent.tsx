import { useEffect, useState } from 'react';
import type { BaseWord } from '../utils/WordInterfaces';
import { fetchWordsFromServer } from '../utils/WordGetter.tsx';
import type {NounMeta} from "../utils/WordInterfaces";

type Props = {
    onWordSelect: (word: BaseWord, meta: NounMeta) => void;
};

export function NounComponent({ onWordSelect }: Props) {
    const [words, setWords] = useState<BaseWord[]>([]);
    const [selectedWord, setSelectedWord] = useState<BaseWord | null>(null);
    const [count, setCount] = useState<'singular' | 'plural'>('singular');

    useEffect(() => {
        fetchWordsFromServer('noun').then(setWords);
    }, []);

    const handleConfirm = () => {
        if (selectedWord) {
            onWordSelect(selectedWord, { count });
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

                    <button className="btn-confirm" onClick={handleConfirm}>
                        Zatwierdź Rzeczownik
                    </button>
                </div>
            )}
        </div>
    );
}