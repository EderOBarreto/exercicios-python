from random import randint
from time import sleep
print(37 * '=')
print(10 * '=' +' \033[1;34mSuper JO KEN PO\033[m ' + 10 * '=')
print(37 * '=')

print("""Digite:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura""")

escolha_aleatoria = randint(1, 3)
escolha = int(input('->'))

escolhas = {1: 'pedra',
            2: 'papel',
            3: 'tesoura'}

resultado = 'venceu'
mostrar_resultado = 1

if escolha != 1 and escolha !=2 and escolha != 3:
    mostrar_resultado = 0
    print('Escolha uma opção válida!')
elif escolha == escolha_aleatoria:
    resultado = 'empatou'
elif escolha == (escolha_aleatoria - 2) or escolha == (escolha_aleatoria + 1):
    pass
else:
    resultado = 'perdeu'

if mostrar_resultado:
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print('PO!!!')
    sleep(0.25)
    print('Você escolheu {} ele {}.'.format(escolhas[escolha], escolhas[escolha_aleatoria]))
    print('\033[7;30mVocê {}!\033[m'.format(resultado))
