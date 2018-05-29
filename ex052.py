num = int(input('Digite um número:'))
primo = 1

for i in range(num - 1, 1, -1): # ou (2, num +1 )
    if num % i == 0:
        primo = 0
        break
if primo:
    print('É um número primo.')
else:
    print('Não é um número primo')
