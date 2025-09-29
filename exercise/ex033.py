'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

num1 = int(input('Enter first value: '))
num2 = int(input('Enter second value: '))
num3 = int(input('Enter third value: '))

smaller = num1
bigger = num1

# Verificando qual numero e menor
if num2 < num1 and num2 < num3:
    smaller = num2
if num3 < num2 and num3 < num1:
    smaller = num3

# Verificando qual numero e maior
if num2 > num1 and num2 > num3:
    bigger = num2
if num3 > num1 and num3 > num2:
    bigger = num3

print('The smallest number is: ', smaller)
print('The bigger number is: ', bigger)