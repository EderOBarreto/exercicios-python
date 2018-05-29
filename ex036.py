val_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
# o prazo é em anos
prazo_pagamento = int(input('Digite a quantidade de anos para pagar: '))

val_prestacao = val_casa / (prazo_pagamento * 12)

if val_prestacao <= salario * 0.3:
    print('\033[1;34mEmpréstimo autorizado!\033[m')
else:
    print('\033[1;31mEmpréstimo negado!\033[m')
