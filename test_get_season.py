from get_season import get_season


def test_get_season():
    # Test if valid month returns correct season
    assert get_season("April") == "Spring"
    assert get_season("August") == "Summer"
    assert get_season("September") == "Fall"
    assert get_season("February") == "Winter"

    # Test if passing a non-string value to the function results in a TypeError
    try:
        get_season(3242)
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"

    # Test if passing a invalid month name to the function results in a ValueError
    try:
        get_season("Decembre")  # Typo
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
