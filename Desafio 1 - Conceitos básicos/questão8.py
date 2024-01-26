'''
Um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_mensal = valor_por_hora * horas_trabalhadas

print(f"Seu salário mensal é: R${salario_mensal:.2f}")