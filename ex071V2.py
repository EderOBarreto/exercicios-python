qtdNota50 = qtdNota20 = qtdNota10 = qtdNota1 = 0

print(30 * '-=')
print('{:-^40}'.format('Caixa Eletrônico'))
print(30 * '-=')

valor = int(input('Digite o valor que deseja sacar: '))
while True:

    if valor - 50 >= 0:
        x = valor // 50
        qtdNota50 += x
        valor -= x * 50

    if valor - 20 >= 0:
        x = valor // 20
        qtdNota20 += x
        valor -= x * 20

    if valor - 10 >= 0:
        x = valor // 10
        qtdNota10 += x
        valor -= x * 10

    if valor - 1 >= 0:
        x = valor // 1
        qtdNota1 += x
        valor -= x * 1

    if valor == 0:
        break

print(30 * '-')
tot = qtdNota1 + qtdNota10 + qtdNota20 + qtdNota50
if tot > 0:
    print(f'{qtdNota50} notas de 50, {qtdNota20} notas de 20, {qtdNota10} notas de 10, {qtdNota1} notas de 1')
else:
    print('Valor inválido!')
print(30 * '-')

