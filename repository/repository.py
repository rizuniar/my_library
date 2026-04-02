from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import delete

from models.books import BooksModel 
from schemas.books import SBook, SBookAdd

class BookRepository:
    @classmethod
    async def add_one(cls, data: SBookAdd, session: AsyncSession) -> BooksModel:
        book_dict = data.model_dump()
        book = BooksModel(**book_dict)

        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book 

    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = select(BooksModel)
        result = await session.execute(query)
        books_models = result.scalars().all()
        return books_models

    @classmethod
    async def get_one(cls, id: int, session: AsyncSession):
        query = select(BooksModel).where(BooksModel.id == id)
        result = await session.execute(query)
        book_model = result.scalar_one_or_none()
        return book_model

    @classmethod
    async def update(cls, id: int, data: SBookAdd, session: AsyncSession):
        book_dict = data.model_dump()
        query = update(BooksModel).where(BooksModel.id == id).values(**book_dict).returning(BooksModel)
        result = await session.execute(query)
        new_book = result.scalar_one_or_none()
        await session.commit()
        return new_book

    @classmethod
    async def delete(cls, id: int, session: AsyncSession):
        query = select(BooksModel).where(BooksModel.id == id)
        result = await session.execute(query)
        exists = result.scalar_one_or_none() is not None
        if not exists: return False

        delete_query = delete(BooksModel).where(BooksModel.id == id)
        await session.execute(delete_query)
        await session.commit()

        return True
