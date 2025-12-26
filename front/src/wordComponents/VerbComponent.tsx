import { useEffect, useState } from 'react';
import type { BaseWord } from '../utils/WordInterfaces';
import { fetchWordsFromServer } from '../utils/WordGetter.tsx';

import type {VerbMeta, Person, Tense} from "../utils/WordInterfaces";

type Props = {
    onWordSelect: (word: BaseWord, meta: VerbMeta) => void;
};

export function VerbComponent({ onWordSelect }: Props) {

    const startingMeta: VerbMeta = {
        tense : 'prsimple', person: 'second singular', negation: false
    }

    const [words, setWords] = useState<BaseWord[]>([]);
    const [selectedWord, setSelectedWord] = useState<BaseWord | null>(null);
    const [meta, setMeta] = useState<VerbMeta>(startingMeta);

    useEffect(() => {
        fetchWordsFromServer('verb').then(setWords);
    }, []);

    const handleConfirm = () => {
        if (selectedWord && meta) {
            onWordSelect(selectedWord, meta);
            setSelectedWord(null);
            setMeta(startingMeta);
        }
    };

    const updateMeta = (field: keyof VerbMeta, value: string | boolean) => {
        setMeta(prev => ({
            ...prev,
            [field]: value
        }));
    };

    return (
        <div className="word-component">
            <h3 className="category-title">Wybierz Czasownik</h3>

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
                            Czas:
                            <select
                                value={meta.tense}
                                onChange={(e) => updateMeta('tense', e.target.value as Tense)}
                            >
                                <option value="prsimple">Present Simple</option>
                                <option value="prcontinous">Present Continuous</option>
                                <option value="pasimple">Past Simple</option>
                                <option value="pacontinous">Past Continuous</option>
                                <option value="prperfect">Present Perfect</option>
                                <option value="paperfect">Past Perfect</option>
                                <option value="prperfectc">Present Perfect Continuous</option>
                                <option value="paperfectc">Past Perfect Continuous</option>
                            </select>
                        </label>
                    </div>

                    <div className="form-group">
                        <label>
                            Osoba:
                            <select
                                value={meta.person}
                                onChange={(e) => updateMeta('person', e.target.value as Person)}
                            >
                                <option value="first singular">I (Ja - 1. poj.)</option>
                                <option value="second singular">You (Ty - 2. poj.)</option>
                                <option value="third singular">He/She/It (On/Ona/Ono - 3. poj.)</option>
                                <option value="first plural">We (My - 1. mnoga)</option>
                                <option value="second plural">You (Wy - 2. mnoga)</option>
                                <option value="third plural">They (Oni - 3. mnoga)</option>
                            </select>
                        </label>
                    </div>

                    <div className="form-group checkbox-label">
                        <label style={{ flexDirection: 'row', display: 'flex', gap: '10px', alignItems: 'center' }}>
                            <input
                                type='checkbox'
                                checked={meta.negation}
                                onChange={(e) => updateMeta('negation', e.target.checked)}
                            />
                            Zdanie przeczące (Not)
                        </label>
                    </div>

                    <button className="btn-confirm" onClick={handleConfirm}>
                        Zatwierdź Czasownik
                    </button>
                </div>
            )}
        </div>
    );
}