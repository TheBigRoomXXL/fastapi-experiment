from pydantic import BaseModel, Field


class NoteIn(BaseModel):
    content: str = Field(title="The body of the note")


class NoteOut(BaseModel):
    id: int = Field(title="The primary id of the note")
    content: str = Field(title="The body of the note")
