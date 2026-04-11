from fastapi import FastAPI, status 
from typing import Optional, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
app = FastAPI()

books = [
    {
        "book_id": 1,
        "author": "George Orwell",
        "title": "1984",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English",
    },
    {
        "book_id": 2,
        "author": "Harper Lee",
        "title": "To Kill a Mockingbird",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English",
    },
    {
        "book_id": 3,
        "author": "Paulo Coelho",
        "title": "The Alchemist",
        "publisher": "HarperTorch",
        "published_date": "1988-01-01",
        "page_count": 208,
        "language": "Portuguese",
    },
]


class Book(BaseModel):
    book_id: int
    title: str
    publisher: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    author: str
    title: str
    publisher: str
    published_date: str
    page_count: int
    language: str



@app.get("/get_books")
async def get_all_books() -> List[Book]:
    return books


@app.post("/create_book", status_code= status.HTTP_201_CREATED)
async def create_a_book(book: Book) -> dict:
    new_book= book.model_dump()
    books.append(new_book)

    return new_book


@app.get("/book/{book_id}")
async def find_a_book(book_id: int) :
    for book in books:
        if book["book_id"]== book_id:
            return book

@app.patch("/book/{book_id}")
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

@app.delete("/book/{book_id}")
async def delete_book(book_id: int): 
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)

        return{"done"}

        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "No such book is found in the database.")
    