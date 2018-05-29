from random import randint
tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
maior = tupla[0]
menor = tupla[0]


print(f'Numeros sorteados:', end= ' ')
for n in tupla:
    print(n, end=' ')
ordenados = sorted(tupla)

print(f'\n\nMaior {tupla[4]}\nMenor {tupla[0]}')

