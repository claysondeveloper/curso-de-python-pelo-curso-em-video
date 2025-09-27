'''
 Escreva um programa que faça o computador “pensar”
 em um número inteiro entre 0 e 5 e peça para o
 usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep # importa um temporizador

# Numero sorteado pelo computador
numSorted = random.randint(0, 5)

print('--='*50)
print('I\'m going to think of a number from 0 to 5 try to guess...')
print('--='*50)

# Numero que o usuario escolheu
numSelected = int(input('Enter the number: '))

print('Processing...')
sleep(2) # Temporizador

# Condição se o usuario acertou ou nao
if numSelected == numSorted:
    print('Congratulations you got it right!')
else:
    print('Sorry, you didn\'t get it right!')

print('The number drawn was {}.'.format(numSorted))
print('The and')