
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} X {i} = {num * i}')
    print(15 * '-' + '\n')
print('Volte Sempre!')
