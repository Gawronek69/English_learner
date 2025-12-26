from fastapi import FastAPI
from back.app.utils.english_vocab import *
app = FastAPI()


@app.get("/")
async def root():
    return {"vocab" : {
        "verbs" : {
            "regular" : verbs_regular,
            "irregular" : verbs_irregular_dict,
        },
        "nouns" : {
            "regular" : nouns_regular,
            "irregular" : nouns_irregular_dict,
        },
        "adjectives" : {
            "regular" : adjectives_regular,
            "irregular" : adjectives_irregular_dict,
        },
        "prepositions" : prepositions,
        "conjunctions" : conjunctions,
    }}

@app.post("/")
async def root():
    return {"vocab" : {
    }}

