'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''


def calcular_total(carrinho_compras):
    total = 0
    for produto, quantidade in carrinho_compras.items():
        total += quantidade
    return total

carrinho_compras = {}

while True:
    acao = input("Digite 'a' para adicionar um produto, 'c' para calcular o total, ou 's' para sair: ")

    if acao == 'a':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        carrinho_compras[produto] = quantidade

    elif acao == 'c':
        total = calcular_total(carrinho_compras)
        print("O total do carrinho de compras é: ", total)

    elif acao == 's':
        break

    else:
        print("Ação inválida. Tente novamente.")