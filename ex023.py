num = input('Digite um número de 0 a 9999:')

num = num.zfill(4)

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

num2 = int(input('Digite um número de 0 a 9999: '))

unidade = num2 % 10
dezena = num2 // 10 % 10
centena = num2 // 100 % 10
milhar = num2 // 1000

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
