'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

km = float(input('How many km were covered: '))

if km <= 200:
    valueOfKm = km * 0.50
else:
    valueOfKm = km * 0.45
print('A distance of {} km will be charged R$ {:.2f}'.format(km, valueOfKm))