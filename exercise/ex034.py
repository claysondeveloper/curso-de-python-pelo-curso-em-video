'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores
a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

currentSalary = float(input('What is the current salary R$: '))
newSalary = 0

if currentSalary >= 1250:
    newSalary = currentSalary + (currentSalary * 10 / 100)
else:
    newSalary = currentSalary + (currentSalary * 15 / 100)

print('The new salary is R$ {:.2f}'.format(newSalary))