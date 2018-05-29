vel_carro = int(input('Digite a velocidade do carro: '))

if vel_carro > 80:
    print('Você foi multado.\nO valor da multa é de R$:{:.2f}.'.
          format((vel_carro - 80) * 7.00))
