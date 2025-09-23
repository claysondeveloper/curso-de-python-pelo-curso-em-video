'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math

an = float(input('Entre the angle you want: '))
ra = math.radians(an)

print('The angle of {} has the sine of {:.2f}'.format(an, math.sin(ra)))
print('The angle of {} has the cosine of {:.2f}'.format(an, math.cos(ra)))
print('The angle of {} has the tangente of {:.2f}'.format(an, math.tan(ra)))
