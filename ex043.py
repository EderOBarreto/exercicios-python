peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / altura ** 2

if imc > 40:
    print('Obesidade mórbida.')
elif imc > 30:
    print('Obesidade.')
elif imc > 25:
    print('Sobrepeso.')
elif imc > 18.5:
    print('Peso normal.')
else:
    print('Abaixo do peso.')
