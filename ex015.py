cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde_bold': '\033[1;32m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

qtdKm = float(input('Quantidade de quilometros percorridos: '))
qtdDias = int(input('Quantidade de dias alugado: '))

print('A quantidade a pagar é {}R$: {}{:.2f}'.format(cores['verde_bold'], cores['limpa'], qtdDias * 60 + qtdKm * 0.15))