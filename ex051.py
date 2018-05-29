num = float(input('Digite um número: '))
razao = float(input('Digite a razão: '))

for i in range(1, 11):
    print(num + (i - 1) * razao)
print('FIM!')


num2 = int(input('Digite um número: '))
razao2 = int(input('Digite a razão: '))
decimo = int(num2 + 10 * razao2)

for i in range(num2, decimo, razao2):
    print('{}'.format(i), end=' -> ')
print('FIM!')
