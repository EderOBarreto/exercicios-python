numeros = list()
max = 0
min = 0
for i in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
    if i == 0:
        max = min = numeros[0]

    elif numeros[i] > max:
        max = numeros[i]

    elif numeros[i] < min:
        min = numeros[i]

print(f'\nO maior valor é {max},nas posições', end='')
for p, n in enumerate(numeros):
    if n == max:
        print(f' {p} ', end='')
        
print(f'\nO menor valor é {min},nas posições', end='')
for p, n in enumerate(numeros):
    if n == min:
        print(f' {p} ', end='')


