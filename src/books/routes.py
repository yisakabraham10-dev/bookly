from fastapi import APIRouter
from src.books.book_data import books
from fastapi import status
from src.books.schemas import Book, UpdateBook
from fastapi.exceptions import HTTPException
from typing import List

book_router = APIRouter()


@book_router.get("/")
async def helloworld() -> str:
    return "Helloworld"


@book_router.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@book_router.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book


@book_router.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_LOL_created, detail="Book not found"
    )


@book_router.patch("/book/{book_id}")
async def update_book_data(Updated_data: UpdateBook, book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = Updated_data.title
            book["author"] = Updated_data.author
            book["publisher"] = Updated_data.publisher
            book["page_count"] = Updated_data.page_count
            book["language"] = Updated_data.language

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete("/book/{book_id}")
async def delete_book(book: Book, book_id: int) -> str:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return "Book is removed."
