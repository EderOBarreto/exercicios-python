cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

metros = float(input('Digite a quantidade de metros: '))
print('{}{}m{} são {}{}cm{}'.format(cores['magenta'], metros, cores['limpa'],
                                    cores['sublinhado'], metros * 100, cores['limpa']), end=' ')
print('e {}{}mm{}'.format(cores['amarelo'], metros * 1000, cores['limpa']))
