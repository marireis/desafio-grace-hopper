 #Marina dos Reis Barros Alencar => Desafio-1(Exercícios Conceitos Básicos de Python) - questão 5
'''5. Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

salarioBruto = float(input("Digite o valor (R$) do salário bruto: "))

if(salarioBruto <= 1903.98):
    print("Isento de imposto de renda")
    print("Salario líquido : ", salarioBruto)

elif(1903.99 < salarioBruto <= 2826.65):
    print('Aliquota de 7.5%')
    salarioLiq1 = salarioBruto - salarioBruto*(7.5/100)
    print(f'Salario Liquido: ', salarioLiq1)


elif(2826.66 < salarioBruto <= 3751.05):
    print('Aliquota de 15%')
    salarioLiq2 = salarioBruto - salarioBruto*(15/100)
    print(f'Salario Liquido: ', salarioLiq2)

elif(3751.06 < salarioBruto <= 4664.68):
    print('Aliquota de 22.5%')
    salarioLiq3 = salarioBruto - salarioBruto*(22.5/100)
    print(f'Salario Liquido: ', salarioLiq3)

else:
    print('Aliquota máxima 27.5%')
    salarioLiq4 = salarioBruto - salarioBruto*(27.5/100)
    print(f'Salario Liquido: ', salarioLiq4)

