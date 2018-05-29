print(6 * '=' + '\033[1;34m Cálculo do fatorial \033[m' + 6 * '=')
num = int(input('Digite um número: '))
contador = num - 1
while contador > 0:
    num *= contador
    contador -= 1
print('Resultado {}'.format(num))

"""resultado = num
for c in range(1, num):
    resultado *= c
print('O resultado é {}'.format(resultado))"""
