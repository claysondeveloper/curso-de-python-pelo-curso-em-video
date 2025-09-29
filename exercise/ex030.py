'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

# Numero digitadio pelo usuario
num = int(input('Enter a number: '))

# Vefirica se o resto da divisao por 2 sera zero se sim o numero e par
if num % 2 == 0:
    print('The number {} is pair'.format(num))
else:
    print('The number {} is odd'.format(num))