# Scrivete un programma per stampare il seguente modello usando i cicli for.


def print_asterisks(n:int) -> None:
    """Print n asterisks

    Args:
        n (int): The number of asterisks printed
    """
    l=[]
    [l.append('*') for _ in range(0,n)]
    # To remove "[]" from the printing
    print(" ".join(l))
    

MAX=6
[print_asterisks(i) for i in range(1,MAX)]
[print_asterisks(MAX-i) for i in range(2,MAX)]
