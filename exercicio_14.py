import time

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print("Tentando estabelecer a conexão com o banco de dados!")
    tentativa +=1
    time.sleep(10)
print("Conexão bem-sucedida!")