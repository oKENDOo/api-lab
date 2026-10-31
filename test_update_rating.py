import pytest


STARS_RANGE_ERROR = "number of stars must be between 1 and 5 (inclusive)"


# Updating stars accepts 1 and 5, rejects 0 and 6,
# and a rejected update leaves the rating unchanged.
@pytest.mark.parametrize(
    ("stars", "expected_status"),
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ],
)
def test_update_rating_boundary_values(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    original_stars = rating["stars"]

    res = api.put(path, json={"stars": stars}, headers=auth)

    assert res.status_code == expected_status

    if expected_status == 200:
        assert res.json()["stars"] == stars
    else:
        assert res.json() == {"error": STARS_RANGE_ERROR}

    # Read the rating again to verify what was actually saved.
    res = api.get(path, headers=auth)

    assert res.status_code == 200

    expected_stars = stars if expected_status == 200 else original_stars
    assert res.json()["stars"] == expected_stars