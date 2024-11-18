# Detecção de Anomalias em Dados de Transações

transacao = {'valor': 12000, 'hora': 20}

if transacao ['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação é suspeita. ")

else:
    print("Transação normal. ")