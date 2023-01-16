# Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numeroPensado = random.randint(0,5)
numeroAdivinhado = int(input('Qual o número que eu estou pensando? [0 á 5] '))
if numeroAdivinhado == numeroPensado:
  print('Parabéns, você acertou!')
else:
  print('Infelizmente, você errou.\nO número que eu tinha pensado era {}'.format(numeroPensado))
