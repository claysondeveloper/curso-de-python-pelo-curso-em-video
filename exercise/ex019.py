'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.
'''
import random

a01 = input('Enter the first student: ')
a02 = input('Enter the second student: ')
a03 = input('Enter the third student: ')
a04 = input('Enter the fourth student: ')

lis = [a01, a02, a03, a04]
alRandom = random.choice(lis)

print('The random student is: {}'.format(alRandom))