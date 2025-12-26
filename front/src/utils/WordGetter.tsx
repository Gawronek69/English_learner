import type { BaseWord, WordType } from "./WordInterfaces";

export async function fetchWordsFromServer(type: WordType): Promise<BaseWord[]> {
    await new Promise(resolve => setTimeout(resolve, 100));


    const mockData: Record<string, BaseWord[]> = {
        noun: [
            { type: 'noun', word: 'cat' },
            { type: 'noun', word: 'developer' }
        ],
        verb: [
            { type: 'verb', word: 'codes' },
            { type: 'verb', word: 'debugs' }
        ],
        adj:  [
            { type: 'adj', word: 'fast' },
            {  type: 'adj', word: 'lazy' }
        ],
        prep: [{ type: 'prep', word: 'on' }],
        conj: [{  type: 'conj', word: 'and' }]
    };

    return mockData[type] || [];
}