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

### Weekend Exercises

##### Explain the difference between the three direct unit cases and the API tests.
The 3 direct unit tests run the functions directly with no need for additional setup
The 3 API tests run with contexts i.e. a fresh database

##### Show that tests start with fresh data and do not depend on their execution order.
We can see this is the case as we introduce a test case that the database is empty after
a test case populating the data. We can also check that the database is empty before each run


##### Explain the boundary failure you deliberately introduced and fixed.
The boundary case failed when we set the boundary as <= to now becuase
now <= now is true (now = now). By revering the boundry to < we fixed this
as now < now is false.

##### Record the command, results and one limitation in your lab README.
```shell
 PS C:\Users\daraoyedepo\code\learning\cc\week3-sqlalchemy-api> python -m pytest           
====================================================== test session starts =======================================================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\daraoyedepo\code\learning\cc\week3-sqlalchemy-api
plugins: anyio-4.15.1
collected 11 items                                                                                                                

tests\test_api.py ........                                                                                                  [ 72%]
tests\test_rules.py ...                                                                                                     [100%] 

======================================================== warnings summary ======================================================== 
.venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\daraoyedepo\code\learning\cc\week3-sqlalchemy-api\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================= 11 passed, 1 warning in 1.24s ================================================== 
```

Limitation: Side effects like issues due to CORS or database set up may be missed
