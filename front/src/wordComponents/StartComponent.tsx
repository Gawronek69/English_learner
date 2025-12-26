import type {StateType} from "../AppState.tsx";

type Props = {
    onStart: (state: StateType) => void;
};

export function StartComponent({ onStart }: Props) {
    return (
        <div className="start-container">
            <h2 className="title">Kreator Zdań</h2>
            <p className="description">Rozpocznij naukę budując swoje pierwsze zdanie.</p>

            <div className="buttons">
                <button className="btn-primary" onClick={() => {onStart('NOUN')}}>
                    Rozpocznij od Rzeczownika
                </button>
                <button className="btn-primary" onClick={() => {onStart('ADJ')}}>
                    Rozpocznij od Przymiotnika
                </button>
            </div>
        </div>
    );
}