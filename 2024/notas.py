# {} = Dicionario
notas = {'Alexandre': 7.5, 'Estevão': 8, 'Thiago': 9, 'Renan': 2, 'Marcel': 9.5}

# Mostra a nota de 'Renan"
print(notas['Renan'])

# Mostrar keys
notas(notas.keys())

# Mostrar valores
notas.values()

# Ele detecta se existe com "True" ou "False"
print('Alexandre' in notas)
print('Gui' in notas)

# Se existe, ele modifica
notas['Alexandre'] = 9.5
# Se não existe, ele adiciona
notas['Gui'] = 9

# Deletar
del notas['Alexandre']

# É um print, mostra tudo
print(notas) 

