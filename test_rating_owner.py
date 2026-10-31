def assert_owner_rating_is_unchanged(api, auth, rating):
    """Check that the owner can still read the unchanged rating."""
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=auth)

    assert res.status_code == 200
    assert res.json() == rating


# Another user must not read the owner's rating.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)

    print(f"Other user GET status: {res.status_code}")
    assert 400 <= res.status_code < 500

    assert_owner_rating_is_unchanged(api, auth, rating)


# Another user must not change the owner's rating.
def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(path, json={"stars": 5}, headers=other_auth)

    print(f"Other user PUT status: {res.status_code}")
    assert 400 <= res.status_code < 500

    assert_owner_rating_is_unchanged(api, auth, rating)


# Another user must not delete the owner's rating.
def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)

    print(f"Other user DELETE status: {res.status_code}")
    assert 400 <= res.status_code < 500

    assert_owner_rating_is_unchanged(api, auth, rating)