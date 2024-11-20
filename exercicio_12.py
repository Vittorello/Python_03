numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("O número inserido está incorreto: ")
    numero = int(input("Digite um número entre 1 e 10: "))
print("Número válido!")