# Scrivere un programma che, date due liste, 
# restituisca una lista che contiene solo gli elementi che sono comuni 
# tra le prime due liste (senza duplicati)

def remove_duplicates(*lists:range) -> list:
    tmp=[]
    result=[]
    for l in lists:
        tmp=tmp+l
    [result.append(x) for x in tmp if x not in result]
    return result

# Input
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(remove_duplicates(a, b))