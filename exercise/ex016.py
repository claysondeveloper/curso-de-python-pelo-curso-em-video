'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
'''

from math import trunc

num = float(input('Enter the number: '))

print('The number entered is {} and its whole portion is {}'.format(num, trunc(num)))