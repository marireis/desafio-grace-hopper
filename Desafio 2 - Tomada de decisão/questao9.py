'''9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

#inicializa as variáveis
even_count = 0
odd_count = 0
# enquanto o usuário não digitar zero
while True:
  #solicita ao usuário um número
  number = int(input('Digite um número: '))
  #verifica se o número é zero
  if number == 0:
    break
  #verifica se o número é par
  if number % 2 == 0:
    even_count += 1
  #verifica se o número é ímpar
  else:
    odd_count += 1

#apresenta a quantidade de números pares e ímpares inseridos
print(f'Você inseriu {even_count} números pares e {odd_count} números ímpares')