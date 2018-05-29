from random import randint

vitorias = 0
while True:
    numPlayer = int(input('Diga um valor: '))
    escolha1 = input('Par ou Ímpar [P/I]: ')[0].strip().upper()

    numMachine = randint(0, 10)
    escolha2 = 'P' if escolha1 == 'I' else 'I'

    resultado = ''
    x = 0

    tot = escolha1 + escolha2

    if tot % 2 == 0:
        resultado = 'P'
        vitorias += 1
        x = 1
    else:
        resultado = 'I'
        break

    print(20 * '-')
    print(f'Você jogou {escolha1} e o computador {escolha2}.'
          f' Total de {tot} DEU {resul}.')
    print(20 * '-')
    print('Você perdeu!' if x > 0 else 'Você ganhou!')
print(f'GAME OVER! Você venceu {vitorias} vez(es).')
