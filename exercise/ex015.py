'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

day = int(input('How many days the car was rented: '))
km = float(input('How many km were rented: '))

payable = (day * 60) + (km * 0.15)

print('The total payable is: ', payable)