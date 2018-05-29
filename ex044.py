preco = float(input('Digite o valor do produto: '))

print("""Formas de pagamento:
1 - À vista no dinheiro\cheque.
2 - À vista no cartão.
3 - Parcelado em 2X no cartão.
4 - Parcelado em 3X no cartão""")
escolha = int(input('Forma de pagamento: '))
total = preco
num_parcelas = 1
mostrar_preco = 1

if escolha == 1:
    total *= 0.9
elif escolha == 2:
    total *= 0.95
elif escolha == 3:
    num_parcelas = 2
elif escolha == 4:
    total *= 1.2
    num_parcelas = int(input('Digite o número de parcelas desejadas: '))
else:
    print('Escolha de pagamento inválida!\nTente Novamente...')
    mostrar_preco = 0

if mostrar_preco == 1:
    if escolha == 1 or escolha == 2:
        print('Valor total: R$:{}'.format(total))
    else:
        val_parcela = total / num_parcelas
        print('São {} parcelas de {} reais.'.format(num_parcelas, val_parcela))
