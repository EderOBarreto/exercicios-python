num = int(input('Digite um número:'))

for i in range(1, 11):
    print('\033[7;30m{}\033[m X \033[1;31m{:02}\033[m é \033[1;34m{}\033[m.'
          .format(num, i, num * i))

print('FIM!')