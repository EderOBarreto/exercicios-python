ladoA = float(input('Digite o comprimeto do lado A:'))
ladoB = float(input('Digite o comprimeto do lado B:'))
ladoC = float(input('Digite o comprimeto do lado C:'))


if ladoB + ladoC > ladoA and ladoA + ladoC > ladoB and ladoA + ladoB > ladoC:
    if ladoA == ladoB == ladoC:
        print('É um triângulo equilátero!')
    elif ladoA != ladoB != ladoC != ladoA:
        print('É um triângulo escaleno!')
    else:
        print('É um triângulo isósceles!')
else:
    print('Não é um triângulo!')
