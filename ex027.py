cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde_bold': '\033[1;32m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

nome = input('Digite o seu nome: ').strip().split(' ')

print('Primeiro nome: {}{}{}'.format(cores['azul'], nome[0].capitalize(), cores['limpa']))
print('Último nome: {}'.format(nome[nome.__len__()-1].capitalize()))

