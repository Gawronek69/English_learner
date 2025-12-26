export type AppState = {
    state : StateType,
    stateStep: number
}

export type StateType = 'START' | 'NOUN' | 'VERB' | 'ADJ' | 'PREP' | 'CONJ' | 'END'