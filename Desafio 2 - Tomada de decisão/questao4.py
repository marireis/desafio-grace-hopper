"""4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado."""

while True:
    nota = float(input("Digite a nota do aluno de 0 a 10: "))

    if 0 <= nota <= 10:
        resultado = "Aluno aprovado!" if nota >= 7 else "Aluno reprovado!"
        print(resultado)
        break  # Sai do loop se uma nota válida for fornecida
    else:
        print("Nota inválida!!!Por favor, insira uma nota de 0 a 10.")

