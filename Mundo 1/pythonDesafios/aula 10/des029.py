# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dzendo que ele foi multado.
# A multa vai custar 7 reais por cada km acima do limite.

velocidade = float(input('Digite a velocidade do carro em Km/h: '))

if velocidade > 80:
  multa = (velocidade - 80)*7
  print('Você ultrapassou o limite de velocidade, e recebeu uma multa de R${:.2f}'.format(multa))
else:
  print('Vocês está dentro da velocidade permitida')
