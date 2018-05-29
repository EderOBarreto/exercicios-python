v1 = int(input('Valor 1:'))
v2 = int(input('Valor 2:'))
v3 = int(input('Valor 3:'))
v4 = int(input('Valor 4:'))

tupla = (v1, v2, v3, v4)
pos3 = -1

print('\nNúmero de noves: {0}'.format(tupla.count(9)
                                      if tupla.count(9) != 0
                                      else 0))
for i in range(4):
    if tupla[i] == 3:
        pos3 = i

if pos3 != -1:
    print(f'\nPosição do número 3 é {pos3}')
else:
    print('\nNúmero três não encontrado.')

print('\nNúmeros pares:', end= ' ')
for v in tupla:
    print(v if v % 2 == 0 else '', end= ', ')
