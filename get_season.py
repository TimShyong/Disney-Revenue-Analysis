def get_season(month):
    """
    Calculates the corresponding season given a month

    Parameters
    ----------
    month: string
        The name of the month (e.g. "September")

    Returns
    -------
    string
        The name of the season ("Spring", "Summer", "Fall", "Winter")

    Raises
    ------
    TypeError
        If the input argument month is not of type string
    ValueError
        If the input argument month is not a valid month

    Examples
    --------
    >>> get_season("December")
    Winter

    >>> get_season("August")
    Summer
    """
    # Check if month is a string
    if not isinstance(month, str):
        raise TypeError("Month is not a string")

    # Check if month is valid
    if month not in [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]:
        raise ValueError("Month parameter is not a valid month")

    # Determine Season
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Fall"
