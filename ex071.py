qtdNota100 = qtdNota50 = qtdNota20 = qtdNota10 = qtdNota5 = qtdNota1 = 0

print(30 * '-=')
print('{:-^40}'.format('Caixa Eletrônico'))
print(30 * '-=')

valor = int(input('Digite o valor que deseja sacar: '))

qtdNota100 = valor // 100

qtdNota50 = (valor % 100) // 50

qtdNota20 = (valor % 50) // 20

qtdNota10 = ((valor % 50) % 20) // 10

qtdNota5 = valor % 10 // 5

qtdNota1 = valor % 10 % 5


print(30 * '-')
if qtdNota100 > 0:
    print(f'{qtdNota100:2} notas de 100')
if qtdNota50 > 0:
    print(f'{qtdNota50:2} notas de 50')
if qtdNota20 > 0:
    print(f'{qtdNota20:2} notas de 20')
if qtdNota10 > 0:
    print(f'{qtdNota10:2} notas de 10')
if qtdNota5> 0:
    print(f'{qtdNota5:2} notas de 5')
if qtdNota1 > 0:
    print(f'{qtdNota1:2} notas de 1')
print(30 * '-')
