cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
x = 'lts' if area >= 4 else 'l'
print('Você irá precisar de {} {}{}{} de tinta'.format(area / 2, cores['preto_e_branco'], x, cores['limpa']))
