itens = [1, 2, 3, "parar", 4, 5]

i=0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada!")
        break
    print(f"Processando item,{itens[i]}")
    i+=1