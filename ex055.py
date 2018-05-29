
peso = float(input('Digite o seu peso: '))
maior_peso = peso
menor_peso = peso

for i in range(0, 4):
    peso = float(input('Digite o seu peso: '))
    if maior_peso > peso:
        maior_peso = peso
    if menor_peso < peso:
        menor_peso = peso

print('Menor peso: {}'.format(menor_peso))
print('Maior peso: {}'.format(maior_peso))
