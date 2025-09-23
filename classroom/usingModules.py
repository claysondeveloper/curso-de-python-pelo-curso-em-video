'''
Nessa aula, vamos aprender como utilizar módulos em Python utilizando
os comandos import e from/import no Python. Veja como carregar bibliotecas
de funções e utilizar vários recursos adicionais nos seus programas
utilizando módulos built-in e módulos externos, oferecidos no Pypi.
'''

'''Bliblioteca ultilizada para fazer calculos'''
import math # Importa a blibioteca math e todas suas funcionalidades

# from math import sqrt, ceil, floor  # -----> Ultilizado para importar somente a função desejada

num = int(input('Enter a number: '))

# Adiciona o resultado a equação dentro da variavel
raiz = math.sqrt(num)
print('The square root of {} is equal to {}'.format(num, raiz))

# Formata o valor da raiz arredondando para cima
roundedUpward = math.ceil(raiz)
print('The root rounded upward is {}'.format(roundedUpward))

# Formata o valor da raiz arredondando para baixo
roundedDown = math.floor(raiz)
print('The value of the root rounding down is {}'.format(roundedDown))

print('=-' * 50)

'''Biblioteca que gera números aleatorios'''
import random

# Gera números flutuantes aleatorios
print('The random floating value is: ', random.random())

# Gera números inteiros aleatorios, podendo selecionar o inicio e o fim
print('The random integer value is: ', random.randint(1, 100))

print('=-' * 50)

'''Biblioteca de emoji, esta biblioteca precisa ser intalada pois nao vem nos pacotes do python'''
import emoji # ------> Para ver a lista de emoji acesse o site  https://carpedm20.github.io/emoji/

print(emoji.emojize('Python is :thumbs_up:'))