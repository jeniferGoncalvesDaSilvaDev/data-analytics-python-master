caracteristicas_ia = {
    'inteligencia': 'elevada',
    'rapidez': 'no processamento',
    'conhecimento': 'amplo'
}

caracteristicas_unicornio = {
    'magia': 'poderosa',
    'beleza': 'deslumbrante',
    'forca': 'mistica'
}

# União dos dois dicionários
#usar keys para acessar as chaves dos dicionarios e converter em conjuntos
conjunto_ia = set(caracteristicas_ia.keys())
conjunto_unicornio = set(caracteristicas_unicornio.keys())

print('----------------')
print('Conjuntos IA e Unicornio')
print(conjunto_ia)
print(conjunto_unicornio)

uniao = conjunto_ia.union(conjunto_unicornio)

# Criar um dicionário com a união
uniao_dict = {
    'uniao': uniao,
    'nome': 'Growth specialist at NuvemShop'
}

print('União com IA e Unicornio:')
print(uniao)

print('Dicionário de União:')
print(uniao_dict)

for key, value in uniao_dict.items():
    if key == 'uniao' or key == 'nome':
        print('------------------')
        print(f'{key}: {value}')
    else:
        print('------------------------------')
        print('A entidade e características são diferentes')
        break

    
