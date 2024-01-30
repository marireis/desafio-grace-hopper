'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

idade = int(input("Digite sua idade: "))

if idade < 13:
  print("Você é uma criança.")
elif idade < 21:
  print("Você é um adolescente.")
elif idade < 60:
  print("Você é um adulto.")
else:
  print("Você é um idoso.")
