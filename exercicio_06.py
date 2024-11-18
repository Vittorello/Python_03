texto = input("Digite seu texto: ")
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] +=1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)