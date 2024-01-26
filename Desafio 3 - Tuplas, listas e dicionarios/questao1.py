"""1)Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino".
Caso contrário,ele será classificado como"Inocente"."""

# Perguntas sobre o crime
perguntas =[
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?'
]

# Preenche a lista com as respostas do usuário
respostas = []
for indice, pergunta in enumerate(perguntas):
    resposta = input(f'{pergunta} Digite sim ou não: ').lower()
    respostas.insert(indice, resposta == 'sim')

# Classificação 
positivas = 0
for resposta in respostas:
    if resposta:
        positivas += 1

if positivas == 2:
    print('Classificação Suspeita')
elif 3 <= positivas <= 4:
    print('Classificação : Cúmplice')
elif positivas == 5:
    print('Classificação : Assassino')
else:
    print('Classificação : Inocente')