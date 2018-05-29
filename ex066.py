soma =0
contador =0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'A soma total é {soma}.')
print(f'Foram digitados {contador} números.')
