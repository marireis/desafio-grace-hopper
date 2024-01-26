'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''
def numero_reverso(numero):
    numero = str(numero)    # converte o número em string
    numero = numero[::-1]   # [::-1] inverte a ordem dos caracteres da string
    return numero

numero = int(input('Digite um número: '))
print(numero_reverso(numero))
