# Desafio 1- Conceitos Básicos de Python
'''Q3: Faça um Programa que peça a quantidade de quilômetros, 
transforme em metros, centímetros e milímetros.'''

print('\nConversor de Comprimento\n')
km = float(input('Digite o número de Quilômetros (km) que deseja converter:'))
metros = km * 1000
centimetros = km * 100000
milimetros = km * 1000000
print(f'\n{km} km é igual a: \n\n{metros:,.0f} metros \n\n{centimetros:,.0f} centímetros \n\n{milimetros:,.0f} milímetros\n')