# Print all elements of a given list that are less then 5.
def filtered_list(l:range, f:filter) -> list:
    """A filtered list using f filter.

    Args:
        l (list): The list to be filtered.
        f (filter): The filter function.

    Returns:
        list: The list filtered.
    """
    return list(filter(f, l))

print(filtered_list(list(range(1,10)), lambda x: x<5))    