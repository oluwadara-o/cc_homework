from security import hash_password, verify_password

USER = {"username": "student", "email": "student@example.com", "password": "secret123"}


def test_password_hash():
    hashed = hash_password(USER["password"])
    assert hashed != USER["password"]
    assert verify_password(USER["password"], hashed)
    assert not verify_password("wrong", hashed)


def test_login_and_profile(client):
    registered = client.post("/auth/register", json=USER)
    assert registered.status_code == 201
    assert set(registered.json()) == {"id", "username", "email"}
    login = client.post("/auth/login", json=USER)
    assert login.status_code == 200
    token = login.json()["access_token"]
    profile = client.get("/profile/me", headers={"Authorization": f"Bearer {token}"})
    assert profile.status_code == 200
    assert profile.json() == registered.json()


def test_profile_requires_token(client):
    response = client.get("/profile/me")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}

def test_deny_duplicate_registration(client):
    client.post("/auth/register", json=USER)
    registered = client.post("/auth/register", json=USER)
    assert registered.status_code == 409
    assert registered.json()["detail"] == "Email already registered"

    # will also accept if username is same but email is the different
    registered = client.post("/auth/register", json={**USER, "email": "student2@example.com", "password": "password"})
    assert registered.status_code == 201

def test_deny_wrong_password_login(client):
    client.post("/auth/register", json=USER)
    login = client.post("/auth/login", json={**USER, "password": "password"})
    assert login.status_code == 401
    assert login.json()["detail"] == "Invalid email or password"
    login = client.post("/auth/login", json={**USER, "email": "jennie@blackpink.com"})
    assert login.status_code == 401
    assert login.json()["detail"] == "Invalid email or password"

def test_deny_invalid_registrations(client):
    register = client.post("/auth/register", json={**USER, "email": "bademail"})
    assert register.status_code == 422
    assert (register.json()["detail"][0]['msg'] ==
            "value is not a valid email address: An email address must have an @-sign.")

    register = client.post("/auth/register", json={**USER, "username": "me"})
    assert register.status_code == 422
    assert (register.json()["detail"][0]['msg'] ==
            "String should have at least 3 characters")