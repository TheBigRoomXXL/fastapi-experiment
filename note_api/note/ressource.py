from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from shared.database import get_db
from note.model import Note
from note.schema import NoteIn, NoteOut

# from note.service import service_note as snote

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


@router.post("")
async def create_note(note: NoteIn, db: Session = Depends(get_db)) -> NoteOut:
    new_note = Note(**note.dict())
    db.add(new_note)
    db.commit()
    return new_note


@router.get("")
async def query_notes(db: Session = Depends(get_db)) -> list[NoteOut]:
    query = select(Note)
    notes = db.scalars(query).all()
    db.commit()
    return notes
