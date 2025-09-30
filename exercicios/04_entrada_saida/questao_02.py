nome_produto = input("Digite o nome do produto: ")
valor_unitario = float(input("Digite o preço unitário: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))

valor_total = valor_unitario * quantidade_comprada

porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))
valor_com_desconto = valor_total - (valor_total * porcentagem_desconto / 100)

quantidade_parcelas = int(input("Digite em quantas parcelas deseja pagar: "))
valor_parcela = valor_com_desconto / quantidade_parcelas

print("Resumo da compra:")
print("Produto:", nome_produto)
print("Preço total sem desconto: R$", valor_total)
print("Preço com desconto: R$", valor_com_desconto)
print("Quantidade de parcelas:", quantidade_parcelas)
print("Valor de cada parcela: R$", valor_parcela)