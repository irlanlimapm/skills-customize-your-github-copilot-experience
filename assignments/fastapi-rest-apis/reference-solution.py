"""
Reference solution for the FastAPI Book Management API assignment.
This demonstrates a complete working implementation with all endpoints.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI(
    title="Book Management API",
    description="A RESTful API for managing a collection of books",
    version="1.0.0"
)

# Pydantic model for Book
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int
    isbn: str

# In-memory book storage
books_db: List[Book] = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, isbn="978-0743273565"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960, isbn="978-0061120084"),
    Book(id=3, title="1984", author="George Orwell", year=1949, isbn="978-0451524935"),
]

next_id = 4


@app.get("/", tags=["root"])
def read_root():
    """Welcome endpoint."""
    return {"message": "Welcome to the Book Management API", "docs_url": "/docs"}


@app.get("/books", response_model=List[Book], tags=["books"])
def get_all_books():
    """Retrieve all books from the collection."""
    return books_db


@app.get("/books/{book_id}", response_model=Book, tags=["books"])
def get_book(book_id: int):
    """Retrieve a specific book by ID."""
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")


@app.post("/books", response_model=Book, status_code=201, tags=["books"])
def create_book(book: Book):
    """Create a new book in the collection."""
    global next_id
    book.id = next_id
    next_id += 1
    books_db.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book, tags=["books"])
def update_book(book_id: int, book_data: Book):
    """Update an existing book by ID."""
    for i, existing_book in enumerate(books_db):
        if existing_book.id == book_id:
            book_data.id = book_id
            books_db[i] = book_data
            return book_data
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")


@app.delete("/books/{book_id}", status_code=204, tags=["books"])
def delete_book(book_id: int):
    """Delete a book by ID."""
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")


@app.get("/books/search/by-author", response_model=List[Book], tags=["books"])
def search_by_author(author: str):
    """Search for books by author (query parameter)."""
    results = [book for book in books_db if author.lower() in book.author.lower()]
    return results


@app.get("/books/search/by-year", response_model=List[Book], tags=["books"])
def search_by_year(year: int):
    """Search for books published in a specific year."""
    results = [book for book in books_db if book.year == year]
    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
