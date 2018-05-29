sexo = ''
sair = ''
totMan = 0
totWoman = 0
while sair != 'EXIT':
    sexo = input('Digite o sexo (\033[1;34mM\033[m/\033[1;35mF\033[m): ').strip().upper()
    if sexo == 'M':
        totMan += 1
    elif sexo == 'F':
        totWoman += 1
    else:
        print('ERRO!\nDigite um valor válido!')
        continue
    sair = input('Aperte enter para continuar\n'
                 ' ou digite \033[1;31mexit\033[m para sair:\n->').strip().upper()
print('{} HOMENS\n{} MULHERES'.format(totMan, totWoman))
print('FIM')
