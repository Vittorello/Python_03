# Validação de Dados de Entrada
try:
    idade = int(input("Digite sua idade: "))

    if not 18 <= idade <= 65:
        print("A sua idade não está dentro das validações. ")
        exit()

    else:
        print("Sua idade é válida.", idade)

except ValueError:
    print("Erro, digite uma idade numérica.")
    exit()

try:
    email = input("Digite seu melhor e-mail: ").strip()

    if "@" not in email or "." not in email:
        print("Favor inserir um e-mail válido.")
        exit()

    else :
        print("Seu e-mail é válido.")

except ValueError:
    print("Informe um e-mail válido.")
    exit()