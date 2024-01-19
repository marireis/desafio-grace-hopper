# Larissa Vitória Santos Menezes: Desafio 1 (Exercícios - Conceitos Básicos de Python) - Questão 6

#6. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração: Avião = 600km/h, Carro = 100km/h e Ônibus = 80km/h

# Titulo e função do programa
print("\nExercicios Python - Bootcamp WoMakersCode")
print("Modulo 01: Conceitos Basicos")
print("Questao 6 - Tempo de viagem\n")

# Solicita ao usuário a distância percorrida durante a viagem
distancia = float(input("Digite a distancia que sera percorrida durante a viagem (em km): "))

# Verifica se o valor informado é válido
if distancia <= 0:
    print("Erro! A distancia fornecida deve ser um numero positivo.")

else:
    # Definição da velocidade dos transportes
    v_aviao = 600
    v_carro = 100
    v_onibus = 80

    # Calcula a duração das viagens em horas
    duracao_aviao_h = int(distancia / v_aviao)
    duracao_carro_h = int(distancia / v_carro)
    duracao_onibus_h = int(distancia / v_onibus)

    # Calcula a duração das viagens em minutos
    duracao_aviao_m = round(((distancia / v_aviao) - duracao_aviao_h) * 60)
    duracao_carro_m = round(((distancia / v_carro) - duracao_carro_h) * 60)
    duracao_onibus_m = round(((distancia / v_onibus) - duracao_onibus_h) * 60)

    # Imprime os resultados para o usuário
    print(f"\nDistancia total: {distancia} km")
    print(f"A viagem de aviao tera a duracao de {duracao_aviao_h} hora(s) e {duracao_aviao_m} minuto(s)")
    print(f"A viagem de carro tera a duracao de {duracao_carro_h} hora(s) e {duracao_carro_m} minuto(s)")
    print(f"A viagem de onibus tera a duracao de {duracao_onibus_h} hora(s) e {duracao_onibus_m} minuto(s)\n")