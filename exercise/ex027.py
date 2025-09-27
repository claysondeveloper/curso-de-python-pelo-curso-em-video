'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

name = input('Enter your name: ').strip()

separateName = name.split()

print('Your first name is {}'.format(separateName[0]).capitalize())

print('Your last name is {}'.format(separateName[-1]).capitalize())
