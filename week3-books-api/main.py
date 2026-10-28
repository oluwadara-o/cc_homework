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
