soma = contador = maior = menor = 0
continuar = 'S'

while continuar == 'S':
    num = int(input('Digite um número: '))
    if contador == 0:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    soma += num
    contador += 1
    continuar = input('Deseja continuar [N/S]: ').strip().upper()[0]

print('Maior númerO :{}'.format(maior))
print('Menor número: {}'.format(menor))
print('Média: {}'.format(soma/contador))
