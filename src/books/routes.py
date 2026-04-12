from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel

book_router = APIRouter()

@book_router.get("/get_books")
async def get_all_books() -> List[Book]:
    return books


@book_router.post("/create_book", status_code= status.HTTP_201_CREATED)
async def create_a_book(book: Book) -> dict:
    new_book= book.model_dump()
    books.append(new_book)

    return new_book


@book_router.get("/{book_id}")
async def find_a_book(book_id: int) :
    for book in books:
        if book["book_id"]== book_id:
            return book

@book_router.patch("/{book_id}")
async def update_a_book(book_id: int, updated_book: BookUpdateModel) -> dict:
    for book in books:
        if book["book_id"] == book_id:
            book["author"] = updated_book.author
            book["title"] = updated_book.title
            book["publisher"] = updated_book.publisher
            book["published_date"] = updated_book.published_date
            book["page_count"] = updated_book.page_count
            book["language"] = updated_book.language


            return book

    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "No such book is found in the database.")

@book_router.delete("/{book_id}")
async def delete_book(book_id: int): 
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)

        return{"done"}

        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "No such book is found in the database.")
    