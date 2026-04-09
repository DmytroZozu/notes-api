# Notes API

REST API для менеджера нотаток, побудований за допомогою FastAPI, SQLAlchemy та PostgreSQL.

##  Як запустити через Docker Compose (Рекомендовано)

1. Клонуйте репозиторій.
2. Створіть файл `.env` на основі `.env.example`:
   `cp .env.example .env`
3. Запустіть контейнери:
   `docker compose up --build`
4. Документація API (Swagger) буде доступна за адресою: `http://localhost:8000/docs`

##  Як запустити локально (без Docker)

1. Створіть віртуальне середовище: `python -m venv .venv`
2. Активуйте його: `source .venv/bin/activate` (Linux/Mac) або `.venv\Scripts\activate` (Windows)
3. Встановіть залежності: `pip install -r requirements.txt`
4. Переконайтеся, що у вас запущений локальний PostgreSQL і оновіть `DATABASE_URL` у файлі `.env`.
5. Запустіть сервер: `uvicorn app.main:app --reload`

##  Запуск тестів

Тести використовують ізольовану in-memory базу SQLite.
Для запуску виконайте:
`pytest`

##  Змінні середовища
- `DATABASE_URL` — рядок підключення до БД.
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` — кредо для створення бази в Docker.