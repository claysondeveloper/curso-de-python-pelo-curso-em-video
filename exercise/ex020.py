'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle

al1 = input('First student: ')
al2 = input('Second student: ')
al3 = input('Third student: ')
al4 = input('Fourth student: ')

listAl = [al1, al2, al3, al4]
shuffle(listAl)

print('The order is {}'.format(listAl))