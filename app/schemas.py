from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    title: str = Field(..., max_length=100, description="Заголовок нотатки")
    content: Optional[str] = Field(None, max_length=1000, description="Вміст нотатки")

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    content: Optional[str] = Field(None, max_length=1000)

class NoteResponse(NoteBase):
    id: int
    title: str
    content: Optional[str]
    created_at: datetime

    model_config = {'from_attributes': True}