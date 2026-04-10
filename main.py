from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title : str
    author : str

@app.get("/greet")
async def return_hello( age: int = 0   , name: Optional[str] = "User") -> dict:
    return{"message": f"Hello {name}.",  "age": age} 
@app.post("/create_book")
async def create_book(Book_data: Book) -> dict:
    return {
        "title": Book_data.title,
        "author": Book_data.author
    }