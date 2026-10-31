import pytest


STARS_RANGE_ERROR = "number of stars must be between 1 and 5 (inclusive)"


def assert_json_error(res, expected_status):
    """Check that the API rejects the request with a non-empty JSON error."""
    assert res.status_code == expected_status, res.text

    body = res.json()
    assert "error" in body, body
    assert isinstance(body["error"], str), body
    assert body["error"] != "", body

    return body["error"]


# Base choice: 3 whole-number stars, an existing pizza, and the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id


# C1: a number of stars below 1 or above 5 is rejected.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range_are_rejected(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_RANGE_ERROR}


# C2: decimal stars, text stars, and a missing stars field are rejected.
@pytest.mark.parametrize(
    "new",
    [
        {"stars": 3.5},
        {"stars": "3"},
        {},
    ],
    ids=["decimal", "text", "missing"],
)
def test_stars_with_wrong_type_or_missing_are_rejected(api, auth, pizza_id, new):
    new = {"pizza_id": pizza_id, **new}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert_json_error(res, 400)


# C3: a rating for a pizza that does not exist is rejected.
def test_rating_for_missing_pizza_is_rejected(api, auth):
    new = {"pizza_id": 99999999, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert_json_error(res, 400)


# C4: a request without a token is rejected.
def test_rating_without_token_is_rejected(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new)

    assert_json_error(res, 401)


# C4: a request with a token of the wrong length is rejected.
def test_rating_with_short_token_is_rejected(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    short_auth = {"Authorization": "token short"}

    res = api.post("/api/ratings", json=new, headers=short_auth)

    assert_json_error(res, 401)