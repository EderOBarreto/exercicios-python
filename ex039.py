from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento;

if idade < 18:
    print('Você ainda vai se alistar, faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Você já passou do tempo de alistamento, está {} ano(s) atrasado.'
          .format(idade - 18))
else:
    print('É hora de se alistar!')

