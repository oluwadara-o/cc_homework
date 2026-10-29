from application import create_app

app = create_app()
# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import Session
#
# import models
# from database import engine, get_db
# import schemas
#
# # Create the database tables when the app starts.
# # This uses the Course model from models.py.
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
#
# @app.get("/")
# def home():
#     return {"message": "Week 3 SQLAlchemy API is running"}
#
#
# # @app.get("/courses")
# # def get_courses(db: Session = Depends(get_db)):
# #     # Depends(get_db) asks FastAPI to open a database session for this request.
# #     # Read all courses from the database.
# #     courses = db.query(models.Course).all()
# #     print(type(courses))
# #     return courses
# #
# #
# # @app.get("/courses/{course_id}")
# # def get_course(course_id: int, db: Session = Depends(get_db)):
# #     # Find one course by primary key.
# #     # .first() returns one Course object or None.
# #     course = db.query(models.Course).filter(models.Course.id == course_id).first()
# #
# #     if course is None:
# #         raise HTTPException(status_code=404, detail="Course not found")
# #     print(type(course))
# #
# #     return course
# #
# #
# # @app.post("/courses")
# # def create_course(course_data: dict, db: Session = Depends(get_db)):
# #     # This first version accepts a plain dictionary.
# #     # In Part 3, we will replace it with Pydantic validation.
# #     # The keys must match the JSON fields sent by the client.
# #     course = models.Course(
# #         code=course_data["code"],
# #         title=course_data["title"],
# #         lecturer=course_data["lecturer"]
# #     )
# #
# #     try:
# #         # Add the new object to the session, then commit it to the database.
# #         db.add(course)
# #         db.commit()
# #
# #         # Refresh loads database-generated values such as id.
# #         db.refresh(course)
# #         return course
# #
# #     except IntegrityError:
# #         # If the unique course code is repeated, undo the failed transaction.
# #         db.rollback()
# #         raise HTTPException(status_code=409, detail="Course code already exists")
#
# @app.get("/courses", response_model=list[schemas.CourseResponse])
# def get_courses(db: Session = Depends(get_db)):
#     # response_model tells FastAPI to return a list of CourseResponse objects.
#     # Read all courses from the database.
#     courses = db.query(models.Course).all()
#     return courses
#
#
# @app.get("/courses/{course_id}", response_model=schemas.CourseResponse)
# def get_course(course_id: int, db: Session = Depends(get_db)):
#     # Find one course by primary key.
#     course = db.query(models.Course).filter(models.Course.id == course_id).first()
#
#     if course is None:
#         raise HTTPException(status_code=404, detail="Course not found")
#
#     return course
#
#
# @app.post("/courses", response_model=schemas.CourseResponse, status_code=201)
# def create_course(course_data: schemas.CourseCreate, db: Session = Depends(get_db)):
#     # course_data has already been checked by Pydantic.
#     # We can use dot notation because course_data is a CourseCreate object.
#     course = models.Course(
#         code=course_data.code,
#         title=course_data.title,
#         lecturer=course_data.lecturer
#     )
#
#     try:
#         db.add(course)
#         db.commit()
#         db.refresh(course)
#         return course
#
#     except IntegrityError:
#         db.rollback()
#         raise HTTPException(status_code=409, detail="Course code already exists")
