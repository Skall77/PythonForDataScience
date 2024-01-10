def ft_filter(function, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function is None:
        def replace_function(x):
            return x
        function = replace_function
    return (item for item in iterable if function(item))


# Test
# print(ft_filter.__doc__)
# print(filter.__doc__)

# bool_list = [True, False, True, False, True, False, True, False, True, False]
# print(list(filter(None, bool_list)))
# print(list(ft_filter(None, bool_list)))


# def is_even(x):
#     return x % 2 == 0


# numbers = [-2, 0, 1, 2, 3, 4, 5, 6, 78, 8, 8948488, -9]

# print(list(filter(is_even, numbers)))
# print(list(ft_filter(is_even, numbers)))
