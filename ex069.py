qtdMaiores = 0
qtdHomens = 0
qtdMulher = 0

while True:
    print('     Cadastre uma pessoa')
    print(30 * '-')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    print(30 * '-')
    if idade > 18:
        qtdMaiores += 1
    if sexo == 'M':
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        qtdMulher +=1

    continuar = input('Continuar [N/S]: ').strip().upper()[0]

    if continuar == 'N':
        break
    print(30 * '-' + '\n')

print(f'{qtdMaiores} maiores de idade, {qtdHomens} homen(s) e\n {qtdMulher} mulher(es) menores de 20 anos ')
