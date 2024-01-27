# Luciane Fernandes Roque => Desafio-1(Exercícios Conceitos Básicos de Python) - questão 9
'''9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
'''
#quantidade de horas de exercício físico por semana
hours_per_week = float(input('Digite o numero de horas de exercício físico por semana: '))
if hours_per_week < 0:
    print('O valor deve ser maior que zero')

#convertendo_para_minutos = hours_per_week * 60
minutes_per_week = hours_per_week * 60
#calorias queimadas em um mês
calories = minutes_per_week * 5 * 4
print(f"A quantidade de calorias queimadas em um mês é: {calories:.0f} calorias")
