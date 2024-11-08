# Criando dicionario 'clubes'
clubes = {'Sport': 23, 'Santa Cruz':15, 'Nautico': 17, 'Salgueiro': 13, 'Retro':14, 'Central': 10, 'Decisão': 3, 'America-PE': 5, 'Ypiranga-PE': 3, 'Flamengo Arcoverde': 1}

# Nome detro de 'clube' ja existe? Estou modificando 'clubes'
clubes['Salgueiro'] = 16
clubes['Retro'] = 11

# Nome detro de 'clube' não existe? Estou adicionando 'clubes'
clubes['Ipojuca'] = 4
clubes['Serra Talhada'] = 0

# Deletando 'clubes'
del clubes['Ypiranga-PE']
del clubes['Flamengo Arcoverde']

# Verificando
print(clubes['Sport'])
print(clubes['Salgueiro'])

# Se existe: "True"
# Se não existe: "False"
print('Sport' in clubes)
print('Afogados' in clubes)

print(clubes)