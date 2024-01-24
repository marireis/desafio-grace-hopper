#Aluna: Cintia Andrade
#Desafio 2 - Questão 8

#Criar um programa em Python
#que solicite três números ao usuário,
#ultilizando estruturas condicionais para determinar o maior entre eles
#e apresente o resultado.

while True:
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    num3 = float(input('Digite o último número: '))

    if num1 > num2 and num3:
     print(f'O número {num1} é o maior')
    elif num2 > num1 and num3:
     print(f'O número {num2} é o maior')
    elif num3 > num1 and num2:
     print(f'O número {num3} é o maior')
    continuar = input('Quer continuar S/N: ').upper()[0].strip()
    if continuar[0] == 'N':
      print('Obrigada por interagir comigo!')
      break
    