# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, pi

angulo = float(input('Digite o comprimento do ângulo: '))
angulo = angulo * pi / 180

print('Seno de {:.3f}º\nCosseno de {:.3f}º\nTangente de {:.3f}º'.format(sin(angulo), cos(angulo), tan(angulo)))
