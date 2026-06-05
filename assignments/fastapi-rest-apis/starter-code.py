from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Book Management API", version="1.0.0")

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

# TODO: Implement the following endpoints:

@app.get("/books", response_model=List[Book])
def get_all_books():
    """Retrieve all books from the collection."""
    # Your implementation here
    return books_db


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Retrieve a specific book by ID."""
    # Your implementation here
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    """Create a new book in the collection."""
    # Your implementation here
    global next_id
    book.id = next_id
    next_id += 1
    books_db.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    """Update an existing book by ID."""
    # Your implementation here
    for i, existing_book in enumerate(books_db):
        if existing_book.id == book_id:
            book.id = book_id
            books_db[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """Delete a book by ID."""
    # Your implementation here
    for i, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Book not found")
