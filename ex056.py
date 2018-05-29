soma_idade = 0
maior_idade = 0
nome_mais_velho = ''
mulheres_menores = 0

for i in range(0, 4):
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo(M ou F): ').upper().strip()
    if sexo == 'F' and idade < 21:
        mulheres_menores += 1
    if i == 0 and sexo == 'M' or idade > maior_idade and sexo == 'M':
        nome_mais_velho = nome
    soma_idade += idade

print('Média das idades: {}'.format(soma_idade/4))
print('O homem mais velho é o {}'.format(nome_mais_velho))
print('Número de mulheres menores de idade: {}'.format(mulheres_menores))
