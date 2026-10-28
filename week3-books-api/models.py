from sqlalchemy import Column, Integer, String
from database import Base


# Course is a Python class, but SQLAlchemy maps it to the courses table.
class Book(Base):
    # This is the table name that will be created in SQLite.
    __tablename__ = "books"

    # id is the primary key. SQLite will generate it automatically.
    id = Column(Integer, primary_key=True, index=True)

    # book title, author, and year are required fields.
    title = Column(String,  nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

