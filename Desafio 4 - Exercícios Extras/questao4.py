"""
3) Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta.
"""
def celsius_para_fahrenheit(celsius):
    return (1.8 * celsius) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def exibir_menu():
    print("\nEscolha uma opção:")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Sair")

def saida_menu():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(celsius)
            print(f"\n{celsius} graus Celsius é igual a {resultado:.2f} graus Fahrenheit.")
        elif opcao == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f"\n{fahrenheit} graus Fahrenheit é igual a {resultado:.2f} graus Celsius.")
        elif opcao == '3':
            print("\nSaindo do programa...")
            quit()
        else:
            print("Opção inválida. Por favor, tente novamente.")

saida_menu()