descricao = input("Digite a descrição do produto: ")
preco_compra = float(input("Digite o preço de compra: "))
estoque = int(input("Digite a quantidade em estoque: "))

preco_venda = preco_compra * 2

if estoque > 50:
    preco_venda *= 0.4
elif estoque < 10:
    preco_venda *= 1.4

print("O preço de venda do ", descricao, " é:", preco_venda)
