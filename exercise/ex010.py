'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

value = float(input('How much money do you have in your wallet R$: '))

total = value / 5.30

print('You can have it for {:.2f} dollars.'.format(total))