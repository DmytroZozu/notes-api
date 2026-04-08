from fastapi import FastAPI
from .database import engine, Base
from .routes import router

# Створення таблиць при старті
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API", description="Простий REST API для менеджера нотаток")

app.include_router(router)