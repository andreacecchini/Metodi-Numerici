#Sfruttando la list comprehension, 
# scrivi una riga di codice Python che prende un elenco
# (ad esempio, a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
# e crea un nuovo elenco che ha solo gli elementi pari di questo elenco 
print([x for x in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if x % 2 == 0])