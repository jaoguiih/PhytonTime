# Dicionários
cliente = {
    "1": {"nome": "João", "idade": 18},
    "2": {"nome": "Caio", "idade": 17},
    "3": {"nome": "Pedro", "idade": 19},
    "4": {"nome": "Ana", "idade": 22},
    "5": {"nome": "Luiz", "idade": 16},
    "6": {"nome": "Beatriz", "idade": 26},
    "7": {"nome": "Carlos", "idade": 30},
    "8": {"nome": "Juliana", "idade": 28},
    "9": {"nome": "Kaue", "idade": 21},
    "10": {"nome": "Davi", "idade": 23}
}

produto = {
    "1": {"nome": "Notebook", "preco": 2200},
    "2": {"nome": "Smartphone", "preco": 1200},
    "3": {"nome": "Tablet", "preco": 1500},
    "4": {"nome": "Headphone", "preco": 150},
    "5": {"nome": "Mouse", "preco": 40},
    "6": {"nome": "Teclado", "preco": 80},
    "7": {"nome": "Monitor", "preco": 400},
    "8": {"nome": "Webcam", "preco": 100},
    "9": {"nome": "Microfone", "preco": 180},
    "10": {"nome": "Alto-falantes", "preco": 320}
}

# Vendo se a chave existe
print("Chave 1 existe no dicionário cliente:", "1" in cliente)
print("Chave 15 existe no dicionário produto:", "15" in produto)

# Excluindo clientes e produtos
del cliente["9"]
del cliente["10"]
del produto["8"]
del produto["9"]

# Acrescentar registros
cliente["11"] = {"nome": "Pedro", "idade": 19}
cliente["12"] = {"nome": "Leticia", "idade": 25}
cliente["13"] = {"nome": "Trevisan", "idade": 30}
produto["11"] = {"nome": "Impressora", "preco": 750}
produto["12"] = {"nome": "Scanner", "preco": 400}
produto["13"] = {"nome": "Projetor", "preco": 1000}

# Procurar as chaves
print("Valor da chave 1 no dicionário cliente:", cliente.get("1"))
print("Valor da chave 15 no dicionário produto:", produto.get("15"))

# Ver os valores
print("\nValores do dicionário cliente:")
print(cliente["1"])
print(cliente["2"])
print(cliente["3"])
print(cliente["4"])

print("\nValores do dicionário produto:")
print(produto["1"])
print(produto["2"])
print(produto["3"])
print(produto["4"])