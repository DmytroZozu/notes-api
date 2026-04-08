from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("", response_model=schemas.NoteResponse, status_code=201)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db)):
    db_note = models.Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("", response_model=List[schemas.NoteResponse])
def get_notes(
    limit: int = Query(10, le=100, description="Кількість записів"),
    offset: int = Query(0, ge=0, description="Зміщення"),
    search: str = Query(None, description="Пошук по title та content"),
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Note)
    if search:
        query = query.filter(
            models.Note.title.ilike(f"%{search}%") | 
            models.Note.content.ilike(f"%{search}%")
        )
    return query.offset(offset).limit(limit).all()

@router.get("/{note_id}", response_model=schemas.NoteResponse)
def get_note(note_id: int, db: Session = Depends(database.get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Нотатку не знайдено")
    return note

@router.put("/{note_id}", response_model=schemas.NoteResponse)
def update_note(note_id: int, note_update: schemas.NoteUpdate, db: Session = Depends(database.get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Нотатку не знайдено")
    
    update_data = note_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_note, key, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(database.get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Нотатку не знайдено")
    
    db.delete(db_note)
    db.commit()
    return None