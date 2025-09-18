'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

import math

number = int(input('Enter the number: '))

print('The double of the number is {}'.format(2 * number))
print('The triple os the number is {}'.format(3 * number))
print('The square root of the number is {:.2f}'.format(math.sqrt(number)))