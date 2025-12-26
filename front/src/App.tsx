import { useState } from 'react'
import './App.css'
import {StartComponent} from "./wordComponents/StartComponent.tsx";
import {NounComponent} from "./wordComponents/NounComponent.tsx";
import {AdjectiveComponent} from "./wordComponents/AdjectiveComponent.tsx";
import {PrepComponent} from "./wordComponents/PrepComponent.tsx";
import {ConjComponent} from "./wordComponents/ConjComponent.tsx";
import {VerbComponent} from "./wordComponents/VerbComponent.tsx";
import {EndComponent} from "./wordComponents/EndComponent.tsx";
import type {BaseWord, Word, Meta} from './utils/WordInterfaces.tsx'



type AppState = {
    state : stateType,
    stateStep: number
}

type stateType = 'START' | 'NOUN' | 'VERB' | 'ADJ' | 'PREP' | 'CONJ' | 'END'

function App() {
    const startState : AppState = {
        state: "START",
        stateStep: 0,
    }

    const [words, setWords] = useState<Word[]>([])

    const [appState, setAppState] = useState<AppState>({
        state: 'START',
        stateStep: 0
    })

    function handleAppStateChange() {

        if (words.length - 1 === 0) {
            setAppState(startState)
            setWords([])
        }

        setWords(words.slice(0, appState.stateStep))

        const currentWord: Word = words[words.length - 1]

        setAppState((prevState: AppState) => { return {
            state: currentWord.type.toUpperCase() as stateType,
            stateStep: prevState.stateStep - 1
        }})
    }

    function start(){
        setAppState({
            state : "NOUN",
            stateStep: 1
        })
    }

    function reset(){
        setWords([])
        setAppState(startState)
    }

    function createWord(baseWord: BaseWord, meta: Meta){
        const newWord: Word = {
            id: words.length + 1,
            ...baseWord,
            meta: meta,
        }

        const newState: AppState = {
            stateStep: appState.stateStep + 1,
            state: baseWord.type.toUpperCase() as stateType,
        }

        setAppState(newState)
        setWords([...words, newWord])
    }

    function nextState(nextState: string){

        const newState: AppState = {
            stateStep: appState.stateStep + 1,
            state: nextState.toUpperCase() as stateType,
        }

        setAppState(newState)
    }

    return (
        <div>
            <header>

            </header>
            {appState.state === 'START' && (
                <StartComponent onStart={start}/>
            )}
            {appState.state === 'NOUN' && (
                <NounComponent onWordSelect={createWord}/>
            )}
            {appState.state === 'VERB' && (
                <VerbComponent onWordSelect={createWord}/>
            )}
            {appState.state === 'ADJ' && (
                <AdjectiveComponent onWordSelect={createWord}/>
            )}
            {appState.state === 'PREP' && (
                <PrepComponent onWordSelect={createWord}/>
            )}
            {appState.state === 'CONJ' && (
                <ConjComponent onWordSelect={createWord}/>
            )}
            {appState.state === 'END' && (
                <EndComponent finalWords={words} onReset={reset}/>
            )}
            {appState.stateStep > 0 && (
                <button onClick = {handleAppStateChange}></button>
            )}
            <footer>

            </footer>
        </div>
    )
}

export default App
