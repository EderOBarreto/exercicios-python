from random import randint

num_sorteado = 0
num_escolhido = -1
contador = 0

while num_sorteado != num_escolhido:
    if contador != 0:
        print('É uma pena! Você errou!')
    contador += 1
    num_sorteado = randint(0, 10)
    num_escolhido = int(input('Digite um número de 0 a 10 : '))
    print('O número sorteado foi {}.'.format(num_sorteado))

print('Parabens! Você acertou!')
print('Número de tentativas {}'.format(contador))
print(6 * '-' + 'FIM' + 6 * '-')
