cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde_bold': '\033[1;32m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

distancia = int(input('Digite a distância da viagem: '))

if distancia > 200:
    print('{}O preço da viagem é R$: {}{}'.format(cores['sublinhado'], 0.45 * distancia, cores['limpa']))
else:
    print('{}O preço da viagem é R$: {}{}'.format(cores['preto_e_branco'], 0.5 * distancia, cores['limpa']))
