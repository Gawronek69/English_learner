import uvicorn
from fastapi import FastAPI
from utils.english_vocab import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/words")
async def root():
    return get_full_vocab()

@app.get("/words/{vocab_type}")
async def root(vocab_type: str):
    return get_vocab_by_type(vocab_type)
@app.post("/")
async def root():
    return {"vocab" : {
    }}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)