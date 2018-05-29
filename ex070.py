menorVal = total = qtdProd = cont = 0
nomeMenorVal = ''

while True:
    print('         LER PRODUTO')
    print(30 * '-')
    nome = input('Digite o nome: ')
    preco = float(input('Digite o preco: ').strip())
    print(30 * '-')
    cont += 1

    if cont == 1 or preco < menorVal:
        menorVal = preco
        nomeMenorVal = nome

    if preco > 1000:
        qtdProd += 1

    total += preco
    continuar = input('Continuar [N/S]: ').strip().upper()[0]
    print(30 * '-')

    if continuar == 'N':
        break

print(f'Total: R$:{total:.2f}.')
print(f'{qtdProd} produtos com valor superior a R$:1000,00.')
print(f'{nomeMenorVal} é o produto mais barato.')