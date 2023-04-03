# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto: R$'))
formaPagamento = int(input('''Escolha a forma de pagamento:
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros
'''))
novoPreco = 0
match formaPagamento:
  case 1:
    novoPreco = preco - (preco*10/100)
  case 2:
    novoPreco = preco - (preco*5/100)
  case 3:
    novoPreco = preco
  case 4:
    novoPreco = preco + (preco*20/100)

print(f'O valor a ser pago pelo produto será de R${novoPreco}')