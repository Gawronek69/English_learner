import os
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

current_file = Path(__file__).resolve()
app_dir = current_file.parent
project_root = app_dir.parent

sys.path.append(str(project_root))

from app.utils.english_vocab import *
from app.schemas import WordInput

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

@app.post("/sentence", response_model=list[str])
async def root(sentence: list[WordInput]):
    processed_words = []
    logger.info("Got sentence: %s", sentence)
    for word in sentence:
        processed_word = process_word(word)
        processed_words.append(processed_word)
    logger.info("Processed words: %s", processed_words)
    return processed_words

dist_dir = os.path.join(os.path.dirname(__file__), "..", "dist")

if os.path.isdir(dist_dir):

    assets_dir = os.path.join(dist_dir, "assets")
    if os.path.isdir(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")


    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        file_path = os.path.join(dist_dir, full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)

        return FileResponse(os.path.join(dist_dir, "index.html"))

else:
    print(f"BŁĄD: Nie znaleziono folderu {dist_dir}. Upewnij się, że ścieżka jest dobra i zrobiłeś 'npm run build'.")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)