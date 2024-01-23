'''6. Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.'''
#enquanto o login e a senha não forem iguais a admin e admin123, o programa deve pedir novamente
while True:
    login = input('Digite o login: ')
    password = input('Digite a senha: ')
    if login == 'admin' and password == 'admin123':
        print('Acesso permitido')
        break
    else:
        print('Login ou senha inválidos')
