'''Faça um Programa que peça dois números e imprima o maior deles.'''

#funçao que compara os numeros digitados pelo usuario
def comparar(a, b): 
    if a > b:
        return a
    else:
        return b

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior_num = comparar(num1, num2) #Aqui a gente chama a funçao para fazer a comparaçao
print("O maior número é: ", maior_num) #Retorna o maior numero