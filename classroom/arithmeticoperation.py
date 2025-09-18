'''
Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência
dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação,
divisão, exponenciação e quociente na linguagem Python.
'''

# Ordem de precedencia

'''
1 - ( )
2 - **
3 - * ,  / , // , %
4 - + , -
'''

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

s = num1 + num2      # Sum
d = num1 / num2      # Division
m = num1 * num2      # Multiplication
di = num1 // num2    # Whole division
e = num1 ** num2     # Power

print('The sum of the first number and second number is: {}'.format(s))
print('The division of the first number and second number is: {}'.format(d))
print('The multiplication of the first number and second number is: {}'.format(m))
print('The hole division of the first number and second number is: {}'.format(di))
print('The power of the first number and second number is: {}'.format(e))