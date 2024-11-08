
# Nome e senha
usuario = input('insira seu usuario: ')
print(usuario)
senha = input('digite sua senha: ')
print(senha)

# Senha diferente do nome
while usuario==senha:
    print('ERRO, digite uma senha diferente do nome de usuario')
    print('Digite sua senha novamente')
    usuario = input('insira seu usuario: ')
    senha = input('digite sua senha: ')