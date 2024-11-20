vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "videogames", "valor": 4500},
    {"categoria": "videogames", "valor": 2650}
    
]

totais_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in totais_por_categoria:
        totais_por_categoria[categoria] += valor
    else:
        totais_por_categoria[categoria] = valor

print(totais_por_categoria)