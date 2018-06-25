valores = []

for i in range(0, 5):
    num = int(input('Digite um número: '))
    if i == 0 or num > max(valores):
        valores.append(num)
        print(f'Adicionado na posição {len(valores)-1}.')
    else:
        for p, n in enumerate(valores):
            if num <= n:
                valores.insert(p, num)
                print(f'Adicionado na posição {p}.')
                break
print('-=' * 25)
print(f'Os valores digitados foram: {valores}')
