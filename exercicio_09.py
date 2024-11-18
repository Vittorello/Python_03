# Lista vertical
lista = range(1,11)
for listas in lista:
    if listas % 2 == 0:
        print(listas)


# Lista horizontal
lista = range(1,11)
pares = [x for x in lista if x % 2 == 0]
print(pares)