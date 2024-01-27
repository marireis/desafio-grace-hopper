# Larissa Vitória Santos Menezes: Desafio 1 (Exercícios - Conceitos Básicos de Python) - Questão 6 

# 4. Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.

# Titulo e função do programa
print("\nExercicios Python - Bootcamp WoMakersCode")
print("Modulo 03: Tuplas, listas e dicionários")
print("Questao 4 - Lista de contatos\n")

# Declaração do dicionário que armazenará os contatos do usuário
contatos = {}

print("- Adicione seus contatos!\n")

# Loop para adicionar contatos
while True:
    # Recebe os dados do usuário e os armazena
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contatos[nome] = telefone
    # Quebra do loop
    continuar = input("Digite 0 para parar ou qualquer outro caractere para continuar: ")
    if continuar == "0":
        break

print("\n- Busque seus contatos por nome!")

# Loop para buscar contatos
while True:
    # Recebe o nome
    nome = input("Digite o nome do contato: ")
    # Checagem do nome
    if nome in contatos:
        print(f"Telefone de {nome}: {contatos[nome]}")
    else:
        print("Nome invalido.")
    # Quebra do loop
    continuar = input("Digite 0 para parar ou qualquer outro caractere para continuar: ")
    if continuar == "0":
        break