from pydantic import BaseModel, ConfigDict, Field


# Data accepted when creating a course.
# This schema describes the request body for POST /courses.
class BookCreate(BaseModel):
    # Field adds validation rules before the route function runs.
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    year: int = Field(ge=1900)  # Year must be after 1900


# # Data returned by the API.
# # This schema describes the response shape sent back to the client.
# class CourseResponse(BaseModel):
#     id: int
#     code: str
#     title: str
#     lecturer: str
#
#     # This allows Pydantic to read values from SQLAlchemy objects.
#     model_config = ConfigDict(from_attributes=True)