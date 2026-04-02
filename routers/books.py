from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from schemas.books import SBookAdd, SBook
from repository.repository import BookRepository 

router = APIRouter(
    prefix="/books",
    tags=["Книги"]
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=SBook)
async def create_book(book: SBookAdd, session: SessionDep):
    book_model = await BookRepository.add_one(book, session)
    return book_model 

@router.get("", status_code=status.HTTP_200_OK, response_model=list[SBook])
async def get_all_books(session: SessionDep):
    books = await BookRepository.get_all(session)
    return books

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=SBook)
async def get_book_by_id(id: int, session: SessionDep):
    book = await BookRepository.get_one(id, session)
    if book: return book
    else: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена")

@router.put("/{id}", response_model=SBook)
async def update_book(id: int, data: SBookAdd,session: SessionDep):
    book = await BookRepository.update(id, data, session)
    if book: return book
    else: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена")
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int, session: SessionDep):
    book = await BookRepository.delete(id, session)
    if book: return
    else: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена")
