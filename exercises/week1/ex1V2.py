# Print all elements of a given list that are less then 5.

def less_then_five(l:range) -> list:
    """Return a list of elements less then 5.

    Args:
        l (list): The list of numbers.

    Returns:
        list: The list of elements less then 5.
    """
    return [num for num in l if num < 5]


print(less_then_five(list(range(1, 10))))