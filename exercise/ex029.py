'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

# Km digitado pelo usuario
km = float(input('Enter the speed: '))

# Condição se o km esta a baixo de 80 ou nao
if km < 80:
    print('You are at the speed limit, have a good trip!')
else:
    print('You are not ate the speed limit, the limit is 80 km/h!')
    print('You are at {} km/h!'.format(km))

    s = (km - 80) * 7 # Calcula o valor de 7 por km ecedido

    print('And you will be fined R$ {:.2f}'.format(s))

