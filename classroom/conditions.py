'''
Nessa aula, vamos aprender como utilizar estruturas condcionais simples e compostas nos seus programas em Python.
'''

name = input('Enter your name: ').strip()

if name.upper() == 'CLAYSON':
    print('What a beautiful name you have!')
else:
    print('Your name is so normal!')
print('Nice to meet you {}!'.format(name))