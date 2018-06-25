valores = []
opcao = ''
while opcao != 'N':
    valores.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar? [S/N]:')).strip().upper()

print(f'{len(valores)} números foram digitados.')
valores.sort(reverse=True)
print(f'Lista decrescente = {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')