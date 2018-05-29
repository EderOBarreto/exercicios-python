num = contador = soma = 0
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número: '))
print('Números digitados: {}'.format(contador))
print('Total: {}'.format(soma))
