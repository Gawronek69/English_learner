from pydantic import BaseModel


class WordInput(BaseModel):
    id: int
    type: str
    word: str
    meta: dict[str, str | bool] | None

    def __str__(self):
        return self.word