from pydantic import BaseModel

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
