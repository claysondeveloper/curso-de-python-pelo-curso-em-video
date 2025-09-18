'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
'''

value = input('Enter your value: ')
print('The primitive type of this value is, ', type(value))
print('There are oly spaces, ', value.isspace())
print('Is it a number? ', value.isnumeric())
print('Is it a alphanumeric? ', value.isalnum())
print('Is it a alphabet? ', value.isalpha())
print('Is in capital letter? ', value.isupper())
print('Is in lowercase letter? ', value.islower())
print('Is capitalized? ', value)