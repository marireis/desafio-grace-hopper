#Desafio 2-  Tomada de Decisão
''' Q6: Crie um programa que solicite ao usuário um login e uma senha. 
O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", 
caso contrário imprima uma mensagem de erro.'''

print('\nPara acessar o programa faça o seu Login.\n')
usuario = input('Digite seu nome de usuário:')
senha = input('\nDigite sua senha:')
if usuario == 'admin' and senha == 'admin123':
  print ('\nAcesso permitido!\n\nSeja bem vindo Admin. Você está logado no programa Grace Hopper 2.4.')
else: 
    print ('\nUsuário ou senha incorretos. Por favor, tente novamente.')