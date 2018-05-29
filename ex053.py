frase = input('Digite uma frase:').replace(" ", "").upper()

if frase[::-1] == frase:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo!')

