from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
from database import engine, get_db
import schemas

# Create the database tables when the app starts.
# This uses the Course model from models.py.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Books API is running"}

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    # Depends(get_db) asks FastAPI to open a database session for this request.
    books = db.query(models.Book).all()
    print(type(books))
    return books

@app.get("/books/{books_id}")
def get_course(books_id: int, db: Session = Depends(get_db)):
    # Find one course by primary key.
    # .first() returns one Course object or None.
    book = db.query(models.Book).filter(models.Book.id == books_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Course not found")
    print(type(book))

    return book

@app.post("/books", status_code=201)
def create_course(book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    # course_data has already been checked by Pydantic.
    # We can use dot notation because course_data is a CourseCreate object.
    book = models.Book(
        author=book_data.author,
        title=book_data.title,
        year=book_data.year
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book