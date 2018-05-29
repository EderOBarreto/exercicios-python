nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print('\033[1;31mREPROVADO\033[m')
elif media < 7:
    print('\033[1;32mRECUPERAÇÃO\033[m')
else:
    print('\033[1;34mAPROVADO\033[m')
