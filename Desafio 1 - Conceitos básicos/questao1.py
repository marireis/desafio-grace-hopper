'''
Exercícios Conceitos Básicos de Python
Questão 1. Faça um Programa que peça dois números, realize as principais 
operações soma, subtração, multiplicação, divisão
'''
print("OPERAÇÕES MATÉMATICAS")
print("Soma, subtração, multiplicação e divisão\n")

# Entrada dos valores a ser calculado
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

# Operações matemáticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Saída dos valores calculados
print(f"\nA soma dos números {numero1} e {numero2} é igual a ", soma)
print(f"A subtração dos números {numero1} de {numero2} é igual a ", subtracao)
print(f"A multiplicação dos números {numero1} por {numero2} é igual a ", multiplicacao)
print(f"A divisão dos números {numero1} por {numero2} é igual a {divisao:.2f}")