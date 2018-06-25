nums = []
pares = []
impares = []
opcao = ''
while opcao != 'N':
    nums.append(int(input('Digite um número: ')))
    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()

for n in nums:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('-_' * 20)
print(f'Todos os números : {nums}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
