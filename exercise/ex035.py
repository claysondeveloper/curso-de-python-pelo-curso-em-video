'''
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
'''

seg01 = float(input('Enter the first segment: '))
seg02 = float(input('Enter the second segment: '))
seg03 = float(input('Enter the third segment: '))

if seg01 < seg02 + seg03 and seg02 < seg01 + seg03 and seg03 < seg01 + seg02:
    print('The reported segments form a triangle')
else:
    print('The reported segments do not form a triangle')