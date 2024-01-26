#Aluna: Cintia Andrade
#Desafio 4 - Questão 4
#Criar um programa que leia quanto dinheiro uma pessoa tem na carteira,
#calcule quanto poderia comprar de cada moeda estrangeira. 
#Considerando a tabela de conversão abaixo:
#Dólar Americano: R$ 4,91 Peso Argentino: R$ 0,02 Dólar Australiano: R$ 3,18 
#Dólar Canadense: R$ 3,64 Franco Suiço: R$ 0,42 Euro: R$ 5,36
#Libra esterlina: R$ 6,21

dolar_americano = 4.91
peso_argentino = 0.02
dolar_australiano = 3.18
dolar_canadense = 3.64
franco_suiço = 0.42
euro = 5.36
libra_esterlina = 6.21

dinheiro = float(input('Quanto dinheiro você tem na carteira: R$ '))
print()
print(f'Com este valor você poderá comprar US$ {dinheiro/dolar_americano :.2f} dólares')
print(f'Com este valor você poderá comprar AR$ {dinheiro/peso_argentino :.2f} pesos')
print(f'Com este valor você poderá comprar A$ {dinheiro/dolar_australiano :.2f} dólares australianos')
print(f'Com este valor você poderá comprar C$ {dinheiro/dolar_canadense :.2f} dólares canadenses')
print(f'Com este valor você poderá comprar CHF {dinheiro/franco_suiço :.2f} francos')
print(f'Com este valor você poderá comprar € {dinheiro/euro :.2f} euros')
print(f'Com este valor você poderá comprar GBP {dinheiro/libra_esterlina :.2f} libras esterlinas')
