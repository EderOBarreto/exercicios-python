print(10 * '=' + ' {}Convertendo Números{} '.
      format('\033[1;34m', '\033[m') + 10 * '=')

num = int(input('Digite um número: '))

print('\n1 - Binário.\n2 - Octal\n3 - Hexadecimal\n')

escolha = int(input('Escolha a base de conversão:'))

if escolha == 1:
    print('{} em binário é {}'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('{} em octal é {}'.format(num, oct(num)[2:]))

elif escolha == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:].upper()))

else:
    print('\033[1;31mEstá escolha não existe!\033[m')
