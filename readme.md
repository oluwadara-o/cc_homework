Submission for week3-books-api

Before Running
```shell
cd week3-books-api
python -m venv .venv 
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Paths included in the project:
GET /
GET /books
GET /books/{books_id}
POST /books

Missing features:
- No BookResponse model is defined, so the response model for GET /books and GET /books/{books_id} is not specified.

To run the application, use the following command:
```shell
uvicorn main:app --reload
```

[x] the app starts without errors
[x] SQLAlchemy creates the books table
[x] valid books can be inserted
[x] invalid data is rejected
[x] missing books return 404
[x] all routes were tested in Postman
[x] you can explain the difference between a SQLAlchemy model and a Pydantic schema

A SQLAlchemy model define the structure of the database table schema and the behaviour
of the fields in the table. It is used to programtically interact with the database (as an alternative to SQL)

The pydantic schema define rules for the data that is sent to and from the API. 
It is used here to define additional rules for the data sent into the database 
but these rules are not enforced by the database itself making it useful for 
defining validation rules for specific pathways