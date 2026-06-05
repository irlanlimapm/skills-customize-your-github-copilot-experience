# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a modern RESTful API using FastAPI to manage a collection of books. Learn how to handle HTTP requests, implement CRUD operations, and work with JSON data in a production-ready Python framework.

## 📝 Tasks

### 🛠️ Create a Book Management API

#### Description
Create a FastAPI application that provides endpoints to manage a collection of books. Your API should support reading, creating, updating, and deleting books. Practice routing, request handling, and response formatting.

#### Requirements
Completed program should:

- Define a `Book` model with fields: `id`, `title`, `author`, `year`, `isbn`
- Implement `GET /books` endpoint to retrieve all books
- Implement `GET /books/{book_id}` endpoint to retrieve a specific book by ID
- Implement `POST /books` endpoint to create a new book
- Implement `PUT /books/{book_id}` endpoint to update an existing book
- Implement `DELETE /books/{book_id}` endpoint to delete a book
- Return proper HTTP status codes (200 for success, 404 for not found, 201 for created)
- Include input validation using Pydantic models

## 📚 Starter files

- `starter-code.py` — minimal scaffolding with FastAPI setup and initial routes
- `sample-books.json` — sample data to seed the in-memory book collection

## ⚙️ Setup & Run

Requires Python 3.7+. Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Run the development server:

```bash
cd assignments/fastapi-rest-apis
uvicorn starter-code:app --reload
```

Then navigate to `http://localhost:8000/docs` to test the API using the interactive Swagger UI.

## ✅ Grading / Checklist

- All required endpoints implemented and working
- Proper HTTP status codes returned
- Pydantic models used for request/response validation
- Code is clean, well-organized, and follows Python naming conventions
- API responses are properly formatted as JSON
- Error handling for missing resources (404 errors)
- Optional stretch: add query parameters for filtering books, add pagination, implement data persistence to a file or database

## 📝 Submission

Place your final Python file(s) in the `assignments/fastapi-rest-apis/` folder and open a pull request following the course instructions.

---

**Tips:** Test each endpoint using the Swagger UI at `/docs` or with tools like `curl` or Postman. Start with GET endpoints, then implement POST/PUT/DELETE.
