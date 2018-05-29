nome = input('Digite um nome:')

print(nome.upper())
print(nome.lower())
print('O numero total de letras é {}'.format(nome.__len__() - nome.count(' ')))
primeiro_nome = nome.split(' ', 3)
print(primeiro_nome[0])
