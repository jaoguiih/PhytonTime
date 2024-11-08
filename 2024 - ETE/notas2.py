notas = ('Alexandre': 7.5, 'Estevão': 8, 'Renan': 2, 'Marcel': 9.5, 'Thiago': 6)

del notas['Alexandre']
del notas['Marcel']

notas['Renan'] = 9.5
notas['Thiago'] = 8.5

print(notas['Renan'])
print(notas['Thiago'])

print(notas.get('João', 'Não encontrado'))
print(notas.get('Pedro', 'Não encontrado'))