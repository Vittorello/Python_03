# Classificação de Dados de Sensor
try: 
    temperatura = float(input("Digite a temperatura: "))
    if temperatura < 18:
        print("Temperatura baixa.")

    elif temperatura >= 18 and temperatura <= 26:
        print("Temperatura média.")

    else:
        print("Temperatura alta")

    if temperatura < 0:
        print("Temperatura negativa")

    else:
        print("Temperatura positiva")

except ValueError:
    print("Valor inserido inválido, digite a temperatura correta. ")