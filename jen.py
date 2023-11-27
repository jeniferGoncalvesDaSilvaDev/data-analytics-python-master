caracteristicas_ia ={
 'inteligencia':'elevada',
 'rapidez':'no processamento',
 'conhecimento':'amplo'
}
print(caracteristicas_ia)
#print('inteligencia')
#print(caracteristicas_ia['inteligencia'])
caracteristicas_unicornio ={
 'magia':'poderosa',
 'beleza':'deslumbrante',
 'forca':'mistica'
}
print(caracteristicas_unicornio)

#uniao dos dois dicionarios 
conjunto_ia = set(caracteristicas_ia)
conjunto_unicornio=set(caracteristicas_unicornio)
print('----------------')
print('conjuntos ia e unicornio')
print(conjunto_ia)
print(conjunto_unicornio)
print('uniao com ia e unicornio ')
uniao = conjunto_ia.union(conjunto_unicornio)
print(uniao)
uniao_dict = {
   'uniao':uniao,
   'nome':'Growth specialist at NuvemShop'
}
print(uniao_dict)
for key, value in uniao_dict.items():
    if key=='uniao' or  key=='nome':
        print('------------------')
        print(f'{key}: {value}')
        
    else:
        print('------------------------------')
        print('a entidade e caracteristicas sao diferentes')
        break 
    
    
