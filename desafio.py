# Cálculo de Bônus com Entrada do Usuário
nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome_usr = input("Digite seu nome: ")

        if len(nome_usr) == 0:
            raise ValueError("O nome não pode estar vazio. ")

        elif any(char.isdigit() for char in nome_usr):
            raise ValueError("O nome não deve conter números. ")
        
        elif nome_usr.isspace():
            print("Foi digitado apenas espaço. ")
        
        else:
            print("Nome válido: ",nome_usr)
            nome_valido = True

    except ValueError as e:
        print(e)
    
while not salario_valido:
    try:
        salario_usr = int(input("Digite o valor do seu salário: "))

        if salario_usr < 0:
            raise ValueError("Digite um valor positivo para o salário. ")
    
        else: salario_valido = True

    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
    
while not bonus_valido:
    try:
        bonus_usr = float(input("Digite o valor do seu bônus: "))

        if bonus_usr < 0:
            print("Digite um valor positivo para o bônus. ")
        
        else:
            bonus_valido = True

    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
    

constante_bonus = int(1000)

calculo_bonus = constante_bonus + salario_usr * bonus_usr

print(f"{nome_usr}, seu salário é R${salario_usr:.2f} e seu bônus final é R${calculo_bonus:.2f}")