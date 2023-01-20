# Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
from math import floor

numero = float(input('Digite um número: '))
parteInteira = floor(numero)
print('O número {} tem a parte inteira {}'.format(numero, parteInteira))
