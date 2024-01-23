'''2. Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.'''

medias = []
media_sete = 0

for i in range(5):
    media = 0
    for j in range(4):
        media += float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    media /= 4
    medias.append(media)
    if media >= 7:
        media_sete += 1

print("\nA média dos alunos foi:")
for i in range(5):
    print(f"Aluno {i+1}: {medias[i]}")

print(f"\n{media_sete} alunos tiveram média maior ou igual a 7.")
    
