import pytest


# A pizza is returned when zero, one, or two tools are excluded.
# The returned pizza must not require an excluded tool.
@pytest.mark.parametrize(
    "excluded",
    [
        [],  # Block: no tools excluded
        ["Knife"],  # Block: exactly one tool excluded
        ["Scissors"],  # Same block, another representative input
        ["Knife", "Pizza cutter"],  # Block: exactly two tools excluded
    ],
)
def test_excluded_tools_are_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


# Defect 1: no pizza can satisfy a request that excludes all tools.
# The API should return 400 with a JSON error, not 500 and an empty body.
@pytest.mark.xfail(
    reason=(
        "Defect 1: excluding all tools returns 500 with an empty body "
        "instead of 400 with a JSON error message."
    ),
    strict=True,
)
def test_all_tools_excluded_are_rejected(api, auth):
    excluded = ["Knife", "Pizza cutter", "Scissors"]

    res = api.post(
        "/api/pizza",
        json={"excludedTools": excluded},
        headers=auth,
    )

    assert res.status_code == 400

    body = res.json()
    assert "error" in body
    assert body["error"] != ""