export type WordType = 'noun' | 'adj' | 'verb' | 'prep' | 'conj'

export type NounMeta = {
    count: 'singular' | 'plural';
};

export type Degree = 'positive' | 'comparative' | 'superlative'
export type AdjMeta = {
    degree: Degree
};

export type Tense = 'prsimple' | 'prcontinous' | 'pasimple' | 'pacontinous' | 'prperfect' | 'paperfect' | 'prperfectc' | 'paperfectc';
export type Person = 'first singular' | 'second singular' | 'third singular' | 'first plural' | 'second plural' | 'third plural';
export type VerbMeta = {
    tense: Tense,
    person: Person,
    negation: boolean,
};

export type Meta = VerbMeta | NounMeta | AdjMeta | null;

export interface Word{
    id: number,
    type: WordType,
    word: string,
    meta: Meta,
}

export interface BaseWord{
    type: WordType,
    word: string,
}


