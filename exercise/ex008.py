'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

m = float(input('Size in meters: '))

print('The size in millimetres: {:.1f}'.format(m * 1000))
print('The size in centimeters: {:.1f}'.format(m * 100))
