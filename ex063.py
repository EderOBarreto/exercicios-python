num = int(input('Digite um número: '))
i = 0
n1 = 0
n2 = 1
fib = 0
while i <= num:
    print('{}'.format(fib), end=' -> ')
    fib = n1 + n2
    n1, n2 = n2, fib
    i += 1
print('FIM!')
