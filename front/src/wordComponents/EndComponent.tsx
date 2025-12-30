import { useState } from 'react';
import type { Word } from '../utils/WordInterfaces';

type Props = {
    finalWords: Word[];
    onReset: () => void;
};

export function EndComponent({ finalWords, onReset }: Props) {
    const [isSending, setIsSending] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [wordsTransformed, setWordsTransformed] = useState<boolean>(false);
    const [transformedWords, setTransformedWords] = useState<string[]>([]);


    const handleSendAndReset = async () => {
        setIsSending(true);
        setError(null);

        try {
            const API_URL = `/sentence`;

            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(finalWords),
            });

            if (!response.ok) {
                throw new Error(`Błąd serwera: ${response.statusText}`);
            }

            const data = await response.json();
            console.log(data);
            setTransformedWords(data);
            setWordsTransformed(true)

        } catch (err) {
            console.error(err);
            setError("Nie udało się wysłać zdania. Sprawdź konsolę.");
        } finally {
            setIsSending(false);
        }
    };

    return (
        <div className="end-container">
            <h2 className="title">Twoje Zdanie</h2>

            <div className="sentence-display">
                {!wordsTransformed && finalWords.map((w) => (
                    <span key={w.id} className={`sentence-word word-${w.type}`}>
                        {w.word}
                    </span>
                ))}
                {wordsTransformed && transformedWords.map((w, index) => (
                    <span key={finalWords[index].id} className={`sentence-word word-${finalWords[index].type}`}>
                        {w}
                    </span>
                ))}
                <span>.</span>
            </div>

            {error && (
                <div className="error-message">
                    {error}
                </div>
            )}

            <div className="actions">
                {isSending ? (
                    <button className="btn-primary" disabled>
                        Wysyłanie...
                    </button>
                ) : (
                    <>
                        <button className="btn-primary" onClick={handleSendAndReset}>
                            Zatwierdź i Wyślij
                        </button>

                        <button className="btn-reset-text" onClick={onReset}>
                            Anuluj i zacznij od nowa
                        </button>
                    </>
                )}
            </div>
        </div>
    );
}