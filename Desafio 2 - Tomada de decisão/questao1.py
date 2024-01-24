'''Faça um Programa que peça dois números e imprima o maior deles.'''

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

max_num = find_max(num1, num2)
print("O maior número é: ", max_num)