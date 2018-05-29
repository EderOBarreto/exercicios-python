algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaços? ',algo.isspace())
print('É um número?',algo.isdigit())
print('É alfanumérico? ',algo.isalpha())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsculas? ', algo.islower())
print('Está capitalizada? ',algo.istitle())

