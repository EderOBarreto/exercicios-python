cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde_bold': '\033[1;32m',
         'magenta': '\033[35m',
         'preto_e_branco': '\033[7;30m',
         'sublinhado': '\033[4m'}

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
menor = n1

if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n1:
    maior = n3

if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n1:
    menor = n3

print('O menor número é {}{}{}'.format(cores['azul'], menor, cores['limpa']))
print('O maior número é {}{}{}'.format(cores['magenta'], maior, cores['limpa']))


