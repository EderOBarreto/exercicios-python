valores = list()
opcao = ''

while opcao != 'N':
    num = int(input('Digite um número: '))
    if num in valores:
        print('Valor duplicado!')
    else:
        valores.append(num)
        print('Valor adicionado!')
    opcao = str(input('Quer continuar [N/S]: ')).strip().upper()

valores.sort()
print('-=' * 25)
print(f'Você digitou os valores: {valores}')
