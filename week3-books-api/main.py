from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
from database import engine, get_db
import schemas

# Create the database tables when the app starts.
# This uses the Course model from models.py.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Books API is running"}
