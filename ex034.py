salario = float(input('Qual é o seu salário: '))

if salario > 1250.00:
    salario *= 1.1
else:
    salario *= 1.15
print('O novo salário é {}'.format(salario))
