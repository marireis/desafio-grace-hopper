'''
Em python, crie uma função chamada contar_vogais que recebe uma string como parâmetro.Implemente a lógica para contar o número de vogais na string e retorne o total de vogais.Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.
'''

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    total_vogais = sum(1 for char in frase if char in vogais)
    return total_vogais

frase_usuario = input("Digite uma frase: ")

resultado = contar_vogais(frase_usuario)
print(f"O número de vogais na frase é: {resultado}") 
