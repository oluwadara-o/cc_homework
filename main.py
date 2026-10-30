from application import create_app

app = create_app()

# from fastapi import FastAPI
#
# import models
# from database import engine
# #from routers import auth
# from routers import auth, profile
#
# # Create the users table if it does not exist.
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
# # All auth routes start with /auth.
# app.include_router(auth.router, prefix="/auth")
# app.include_router(profile.router, prefix="/profile")
#
#
#
#
# @app.get("/")
# def home():
#     return {"message": "Hello Week 4 auth API is running++"}


# $env:JWT_SECRET = "481b894f6b72f5a478086c3640695a1e9593ceda383653f24513c095c803a2b1"

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr, Field
#
# app = FastAPI()
#
#
# # This schema describes the data accepted by /register-preview.
# # A schema is a Python class that says which fields the request body must contain.
# class UserRegister(BaseModel):
#     # Field adds validation rules.
#     # Here, username must be between 3 and 50 characters.
#     username: str = Field(min_length=3, max_length=50)
#
#     # EmailStr checks that the value looks like an email address.
#     # This needs the email-validator package.
#     email: EmailStr
#
#     # password must be at least 6 characters.
#     password: str = Field(min_length=6)
#
#
# @app.post("/register-preview")
# def register_preview(user: UserRegister):
#     # If we reach this point, validation has passed.
#     # FastAPI has already converted the JSON body into a UserRegister object.
#     # Do not return the password in the response.
#     return {
#         "username": user.username,
#         "email": user.email,
#         "message": "Validation passed"
#     }
