import type { MouseEventHandler } from 'react';

type Props = {
    onStart: MouseEventHandler<HTMLButtonElement>;
};

export function StartComponent({ onStart }: Props) {
    return (
        <div className="start-container">
            <h2 className="title">Kreator Zdań</h2>
            <p className="description">Rozpocznij naukę budując swoje pierwsze zdanie.</p>
            <button className="btn-primary" onClick={onStart}>
                Rozpocznij
            </button>
        </div>
    );
}