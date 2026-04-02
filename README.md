# 📖 My Library
Библиотечное CRUD приложение
# 🏃‍♂️ Запуск
1. Клонировать репозиторий
```bash
git clone https://github.com/rizuniar/my_library
```
2. Создать виртуальное окружение
```bash
python -m venv env
. env/bin/activate
```
3. Установка зависимостей
```bash
pip install -r requirements.txt
```
4. Запуск сервера
```bash
uvicorn main:app
```
# 📰 Доступные адреса
Swagger UI документация: http://localhost:8000/docs
ReDoc документация: http://localhost:8000/redoc
# 👷‍♂️ Структура проекта
```
my_library/
├── models
|   ├── __init__.py
│   └── books.py         # Модели SQLAlchemy
├── repository/
|   ├── __init__.py
│   └── repository.py    # Работа с данными
├── routers/
|   ├── __init__.py
│   └── books.py         # Роутер
├── schemas/
|   ├── __init__.py
│   └── books.py         # Pydantic схемы
├── README.md
├── books.db
├── database.py          # Инициализация БД
├── main.py              # FastAPI вход
└── requirements.txt     # Зависимости
```
