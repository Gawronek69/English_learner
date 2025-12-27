import type { BaseWord, WordType } from "./WordInterfaces";

export async function fetchWordsFromServer(type: WordType): Promise<BaseWord[]> {
    const url: string = `http://127.0.0.1:8000/words/${type}`

    try{
        const response = await fetch(url)

        if (!response.ok) {
            throw Error(`Could not fetch word from server: ${url}`);
        }

        let data = await response.json();

        data = data.map((word: string) => {return {type: type as WordType, word: word};});

        console.log(data);

        return data;

    }
    catch(error){
        console.log(error)
    }

    return [];
}