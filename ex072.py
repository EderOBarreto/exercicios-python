unidades = ('um', 'dois', 'três', 'quatro',
            'cinco','seis','sete', 'oito', 'nove')
outros = ('dez', 'onze', 'doze','treze','quatorze','quinze',
          'dezesseis', 'dezeseete', 'dezoito', 'dezenove')
dezenas = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
           'setenta','oitenta','noventa')

num = int(input('Digite um número de 0 à 99: '))

if num > 99:
    print('Numero inválido!')
elif 20 < num:
    print(f'{dezenas[num // 10 - 2]}'.capitalize()
          + f' e {unidades[num % 10 - 1]}.' if num % 10 else '.')
elif num >= 10:
    print(f'{outros[num - 10]}.'.capitalize())
elif num > 0:
    print(f'{unidades[num - 1]}.'.capitalize())

