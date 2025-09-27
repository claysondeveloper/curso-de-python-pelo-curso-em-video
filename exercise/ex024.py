'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

city = input('Enter which city your were born: ').strip()

print(city[0:5].capitalize() == 'Santo')

