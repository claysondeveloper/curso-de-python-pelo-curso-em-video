'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas
Quantas letras ao todo sem considerar espaços
Quantas letras tem o primeiro nome.
'''

name = input('Enter your name: ').strip()

print('Your name in upper is: {}'.format(name.upper()))

print('Your name in lower is: {}'.format(name.lower()))

print('Your name have {} letters'.format(len(name) - name.count(' ')))

divi = name.split()

print('Your first name is: {} and it has {} letters'.format(divi[0], len(divi[0])))



