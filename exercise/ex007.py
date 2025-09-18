'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

note1 = float(input('First note: '))
note2 = float(input('Second note: '))

print('The average grade is {:.1f}'.format((note1 + note2) / 2))