from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento

print('CATEGORIA:')

if idade > 20:
    print('MASTER')
elif idade > 19:
    print('SÊNIOR')
elif idade > 14:
    print('JÚNIOR')
elif idade > 9:
    print('INFANTIL')
else:
    print('MIRIM')
