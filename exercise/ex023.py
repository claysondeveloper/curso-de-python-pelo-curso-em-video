'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

number = int(input('Enter a number: '))

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('The unit is {}'.format(u))
print('The ten is {}'.format(d))
print('The hundred is {}'.format(c))
print('The thousand is {}'.format(m))