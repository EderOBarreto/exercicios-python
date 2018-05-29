from math import sqrt, pow
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt(pow(catOposto, 2) + pow(catAdjacente, 2))
print('O comprimento da hipotenusa é {:.2f}'.format(hip))
