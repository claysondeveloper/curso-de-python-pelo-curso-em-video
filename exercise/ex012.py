'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

value = float(input('Enter the product value R$: '))

desc = value * 0.05
newValue = value - desc

print('The product that cost {:.2f} with a discount of 5%. \nWill coast {:.2f}'.format(value,newValue))