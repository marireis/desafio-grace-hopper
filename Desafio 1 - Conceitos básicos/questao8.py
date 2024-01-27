'''8.Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''
#input() retorna uma string, por isso é necessário converter para float
ganho_por_hora = float(input('Quanto você ganha por hora? '))

numero_de_horas_trabalhadas = float(input('Quantas horas você trabalhou no mês? '))
#Calcula o salário multiplicando o ganho por hora pelo número de horas trabalhadas
salario = ganho_por_hora * numero_de_horas_trabalhadas

print('Seu salário é de R$ {:.2f}'.format(salario))