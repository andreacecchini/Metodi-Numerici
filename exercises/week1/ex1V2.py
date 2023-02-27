def less_then_five(l:list) -> list:
    """Return a list of elements less then 5.

    Args:
        l (list): The list of numbers.

    Returns:
        list: The list of elements less then 5.
    """
    return [num for num in l if num < 5]


print(less_then_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))