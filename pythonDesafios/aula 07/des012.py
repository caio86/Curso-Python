# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
precoSemDesconto = float(input('Digite o preço do produto: '))
precoComDesconto = precoSemDesconto - (precoSemDesconto * 5) / 100
print('O mesmo produto com 5% de desconto vai ficar por R${}'. format(precoComDesconto))
