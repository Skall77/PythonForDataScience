def square(x: int | float) -> int | float:
    """
Return the square of a number.

Arguments:
    x {int | float} -- Number to be squared

Returns:
    int | float -- Squared number
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
Return the exponentuation of a number by himself.

Arguments:
    x {int | float} -- Number to be exponentiated

Returns:
    int | float -- Exponentiated number
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return an object that when called returns the result of
    the arguments calculation

    Arguments:
        x {int | float} -- Number to be used in the calculation
        function {function} -- Function to be used in the calculation

    Returns:
        object -- Object that when called returns the result of
        the arguments calculation
    """
    count = 0

    def inner() -> float:
        nonlocal count, x
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner
