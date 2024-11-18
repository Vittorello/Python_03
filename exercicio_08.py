usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
    {"nome": "Igor", "email": "igor.com"}
]

for usuario in usuarios:
    if usuario["email"] == "" or "@" not in usuario["email"]:
        print(usuario["nome"])

