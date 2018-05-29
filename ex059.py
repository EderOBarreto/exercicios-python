continuar = True
n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
n2 = int(input('DIGITE O SEGUNDO VALOR: '))

while continuar:
    print("""Digite:
    [ 1 ] SOMAR
    [ 2 ] MULTILPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA""")
    escolha = input('->').strip()

    if escolha == '1':
        print('A SOMA DE {} E {} É {}'.format(n1, n2, n1 + n2))
    elif escolha == '2':
        print('A MULTIPLICAÇÂO DE {} E {} É {}'.format(n1, n2, n1 * n2))
    elif escolha == '3':
        print('O maior número é {}'.format(n1 if n1 > n2 else n2))
    elif escolha == '4':
        n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
        n2 = int(input('DIGITE O SEGUNDO VALOR: '))
    elif escolha == '5':
        continuar = False
    else:
        print('Escolha uma opção válida!')
        continue
print('FIM')
