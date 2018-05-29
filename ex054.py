from datetime import date

maiores = 0
menores = 0

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento :'))
    if date.today().year - ano < 18:
        menores += 1
    else:
        maiores += 1
print('Maiores de idade: {}'.format(maiores))
print('Menores de idade: {}'.format(menores))

