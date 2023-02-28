# Scrivere un programma per controllare se tutti i caratteri
# di s1 sono contenuti in s2.
# La posizione del carattere non ha importanza.
# Ad esempio con s1='by' e s2='blueberry' dovrebbe restituire true.
# Al contrario, con s1='byZ' e s2='blueberry' dovrebbe restituire false.

import functools
# Input
s1="by"
s2="bluebarry"
# Output
print(functools.reduce(lambda b1,b2: b1 and b2,[c in s2 for c in s1]))

