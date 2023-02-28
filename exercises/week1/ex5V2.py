# Scrivere un programma per controllare se tutti i caratteri
# di s1 sono contenuti in s2.
# La posizione del carattere non ha importanza.
# Ad esempio con s1='by' e s2='blueberry' dovrebbe restituire true.
# Al contrario, con s1='byZ' e s2='blueberry' dovrebbe restituire false.

# Input
s1="by"
s2="bluebarry"
# Output
print(len(list(filter(lambda x: x in s2, s1))) == len(s1))