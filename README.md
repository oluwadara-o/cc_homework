#### Auth API (for Advanced Cloud Computing: Week 4)

This application is a simple API that allows users to register, login, 
and access their profile. The passwords are hashed into the database for
security and JWT is used for authentication. 
The application uses FastAPI and SQLite (SQLAlchemy).

Python 3.11.9

##### How to run the application

######
Create a virtual environment and install dependencies:

```shell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Generate and set a (32 character) JWT_SECRET to hash your password. Keep this token
secret and do not share it If you lose it, users will not be able to log in.

```shell
python -c "import secrets; print(secrets.token_hex(32))"
$env:JWT_SECRET = "paste-your-generated-value-here"
```  
What the application does and which Python version it needs.
How to create an environment and install dependencies.
How to generate and set JWT_SECRET, using placeholders rather than your actual secret.
How to start the server and use /docs to register, log in and access /profile/me.
How to run pytest, and a short summary of the results.
That SQLite creates auth.db locally and the tests use a separate temporary database.
##### Testing the application
To start the server, run the following command:

```shell
uvicorn main:app --reload
```

Then navigate to http://127.0.0.1:8000/docs (or equvalent host and port)
to test the API endpoints.

Verify the /register, /login and /profile/me endpoints work as expected.




###### Automated Testing

Automated tests are avaialble in the tests directory. 
To run the tests use the following command:
```python -m pytest -q```

Expected reults are shown below:
```shell
(.venv) PS C:\Users\daraoyedepo\code\learning\cc\week4-auth-api> python -m pytest -q
......                                                                                                                                                                                                        [100%]
================================================================================================= warnings summary ================================================================================================= 
.venv\Lib\site-packages\fastapi\testclient.py:1
  C:\Users\daraoyedepo\code\learning\cc\week4-auth-api\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 1 warning in 0.71s

```

