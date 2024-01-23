# Luciane Fernandes Roque => Desafio-4(Exercícios extras) - questão 6
'''6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letrada palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício
'''
#importando a biblioteca random
import random

words = ['python', 'java', 'Ruby', 'javascript']

#escolhendo uma palavra aleatória da lista
random_word = random.choice(words)

#criando uma lista com os espaços em branco
mask_word = ['_' for _ in random_word]
#imprimindo a palavra com os espaços em branco
print(' '.join(mask_word))
#definindo o número de tentativas
max_attempts = 6
#começa com zero
attempts = 0
#enquanto houver tentativas e o '_' estiver na palavra
while attempts < max_attempts and '_' in mask_word:
  word = input('Digite uma letra: ')

  if len(word) == 1:
    if word in random_word:
    #se a letra estiver na palavra, substitui o '_' pela letra
      for i in range(len(random_word)):
        if random_word[i] == word:
          mask_word[i] = word
    else:
      #se a letra não estiver na palavra, aumenta o número de tentativas
      attempts += 1
      print('Você errou! Você tem mais {} tentativas'.format(max_attempts - attempts))
  elif word == random_word: #se a palavra digitada for igual a palavra secreta
    mask_word = list(word)
  else: #se a palavra digitada for diferente da palavra secreta
    attempts += 1
    print('Você errou! Você tem mais {} tentativas'.format(max_attempts - attempts))

  print('Palavra: {}'.format(' '.join(mask_word)))

#se o jogador acertar a palavra
if '_' not in mask_word:
  print('Parabéns, você acertou a palavra!')
else:
  print('Você perdeu! A palavra era {}'.format(random_word))
