'''
Faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez
e em que posição ela aparece a última vez.
'''

phase = input('Enter a phrase: ').strip().upper()

print('The letter A appears {} times'.format(phase.count('A')))

print('The first time the letter A appears is in position {}'.format(phase.find('A') + 1))

print('The last time the letter A appears is in position {}'.format(phase.rfind('A') + 1))