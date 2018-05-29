num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
num_termos = int(input('Digite a quantidade de termos: '))
#soma dos termos
termo = num
i = 0
while i < num_termos:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    i += 1
print('FIM')