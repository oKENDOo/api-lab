import uuid


def make_user():
    name = "lab-" + uuid.uuid4().hex[:12]
    return {"username": name, "password": "Pizza-2026"}


# Creating a second user with the same name is refused.
def test_duplicate_username_is_refused(api):
    user = make_user()

    first = api.post("/api/users", json=user)
    assert first.status_code == 201

    second = api.post("/api/users", json=user)
    assert second.status_code == 400
    assert second.json() == {"error": "username already taken"}


# Logging in with an incorrect password is refused.
def test_login_with_wrong_password_is_refused(api):
    user = make_user()

    created = api.post("/api/users", json=user)
    assert created.status_code == 201

    wrong_password = {
        "username": user["username"],
        "password": "Wrong-password",
    }
    res = api.post("/api/users/token/login", json=wrong_password)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# Creating a user with an empty username is refused.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)

    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}