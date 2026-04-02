from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers.books import router as books_router
from models.books import BooksModel
from database import engine, Model

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    print("DB ready!")
    yield
    print("Server shutdown...")

app = FastAPI(lifespan=lifespan)
app.include_router(books_router)
