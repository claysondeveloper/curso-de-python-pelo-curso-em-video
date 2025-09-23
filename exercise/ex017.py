'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

co = float(input('What is the value of the opposite leg: '))
ca = float(input('What the value of the adjacent leg: '))
hi = (co ** 2 + ca ** 2) ** (1/2)


print('The value of the hypotenuse is {:.2f}'.format(hi))