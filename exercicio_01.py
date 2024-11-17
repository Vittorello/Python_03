# Verificação de Qualidade de Dados

try:
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    if quantidade > 0 and preco > 0:
        print("Valores inseridos estão corretos.")
        exit()
    else:
        print("Valores inseridos estão incorretos, favor verificar novamente.")
        exit()

except ValueError:
    print("Erro: Você deve inserir valores numéricos válidos.")
    exit()