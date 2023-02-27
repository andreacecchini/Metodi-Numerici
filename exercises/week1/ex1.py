# Print all elements of a given list that are less then 5.

def filtered_list(l:list, f:lambda x: bool) -> list:
    """A filtered list using f filter.

    Args:
        l (list): The list to be filtered.
        f (lamda x: bool): The filter function.

    Returns:
        list: The list filtered.
    """
    return list(filter(f, l))

print(filtered_list([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10], lambda x: x<5))    

