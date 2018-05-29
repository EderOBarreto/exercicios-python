listagem = ('Lápis', 1.75, 'Borracha', 2,
            'Caderno', 15.90, 'Estojo', 25,
            'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3,
            'Livro', 34.9)

print('-' * 40)
print(' ' * 11 + 'Listagem de preços')
print('-' * 40)
for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<30}R${listagem[pos+1]:8.2f}')
print('-' * 40)