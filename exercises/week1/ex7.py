import functools

def func(l:list, summ=True, mul=True):
    """Return a tuple containing the sum and the mul of all l's element by default.
    If summ=False returns only the mul.
    If mul=False returns only the sum.
    If summ=False and mul=False returns an empty tuple.
    Args:
        l (list): The list to compute
        summ (bool, optional): A flag indicating if the sum has to be cumputed. Defaults to True.
        mul (bool, optional): A flag indicating if the mul has to be conputed. Defaults to True.

    Returns:
        tuple: A tuple containing sum, mul.
        int: An int containing the sum/mul based on the flags. 
    """
    if summ and mul:
        return sum(l), functools.reduce(lambda x1, x2: x1*x2, l)
    if summ:
        return sum(l)
    if mul:
        return functools.reduce(lambda x1, x2: x1*x2, l)
    return ()

# Input
a=list(range(1,10))
print(func(a))
print(func(a,False, False))
print(func(a, summ=False))
print(func(a, mul=False))

