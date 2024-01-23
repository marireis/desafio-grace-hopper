## Desafio 4- Exercícios Extra de Python
''' Q1: Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.'''

print('\nTotal de Aulas assistidas - No Bootcamp WMC\n')
def soma_aulas(sem1,sem2,sem3):
    total_aulas = sem1 + sem2 + sem3
    print(f'\nParabéns! Você assistiu até o momento {total_aulas} aulas.')
sem1 = int(input('Digite a quantidade de aulas que você assistiu na primeira semana: '))
sem2 = int(input('\nDigite a quantidade de aulas que você assistiu na segunda semana: '))
sem3 = int(input('\nDigite a quantidade de aulas que você assistiu na terceira semana: '))
soma_aulas(sem1, sem2, sem3)