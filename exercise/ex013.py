'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

sal = float(input('Whats is the employee´s salary R$: '))

aum = sal * 0.15
newSal = sal + aum

print('The new salary of employee is {:.2f}.'.format(newSal))