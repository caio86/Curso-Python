# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano: '))
bissexto = (ano % 4) == 0
if bissexto:
  print('O ano {} é bissexto'.format(ano))
else:
  print('O ano {} não é bissexto'.format(ano))

