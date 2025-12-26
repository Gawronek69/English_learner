import type {BaseWord, Word} from "./WordInterfaces.tsx";

export const createWord = (baseWord: BaseWord, id: number): Word => {

    switch(baseWord.type) {
        case "verb":
            return {
                id: id,
                ...baseWord,
                meta : {
                    tense : "present",
                    person: "I",
                    negation: false
                }
            }
        case "noun":
            return {
                  id: id,
                ...baseWord,
                meta: {
                    count: "singular"
                }
            }
        case "adj":
            return {
                id: id,
                ...baseWord,
                meta: {
                    degree: "positive"
                }
            }
        case "conj":
            return {
                id: id,
                ...baseWord,
                meta : {}
            }
        case "prep":
            return {
                id: id,
                ...baseWord,
                meta : {}
            }
        default:
            throw Error("Unknown word type " + baseWord.type)
    }
}