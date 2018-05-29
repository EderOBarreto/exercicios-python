from random import randint

num_sorteado = randint(0, 5)
num_escolhido = int(input('Digite o número: '))

if num_escolhido == num_sorteado:
    print('Parabens! Você acertou!')
else:
    print('É uma pena! Você errou!')
print(3 * '-' + 'FIM' + 3 * '-')
print('O número sorteado foi {}.'.format(num_sorteado))

