from math import cos, sin, tan, radians
angulo = float(input('Digite o ângulo: '))
radianos = radians(angulo)
cosseno = cos(radianos)
seno = sin(radianos)
tangente = tan(radianos)
print('Valor do cosseno: {:.2f}'.format(cosseno))
print('Valor do seno: {:.2f}'.format(seno))
print('Valor do tangente: {:.2f}'.format(tangente))
