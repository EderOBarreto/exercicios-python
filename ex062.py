
num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
num_termos = int(input('Digite a quantidade de termos: '))
#soma dos termos
termo = num
termos_ad = 0
i = 0
while i < num_termos:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    i += 1
    if i == num_termos:
        print('PAUSA')
        print('\nDigite 0 para sair ou digite o número de termos a mais.')
        termos_ad = int(input('->'))
        if termos_ad != 0:
            num_termos += termos_ad
print('Progressão finalizada com {} termos mostrados'.format(num_termos))

