# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprétimo será negado.

valorCasa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar pela casa? '))

parcelaMensal = (valorCasa / anos) / 12
if parcelaMensal > (salario * 0.3):
  print('Infelizmente você não pode financiar essa casa')
else:
  print('Financiamento concluido')
  print(f'A parcela mensal a ser paga será de R${parcelaMensal:.2f}')