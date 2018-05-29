n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número: '))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

print('A soma de dois números é {}{}{}!'.
      format(cores['preto_e_branco'], (n1 + n2), cores['limpa']))
