# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo calcule
# e mostre o comprimento da hipotenusa.

from math import sqrt, pow

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(oposto, 2) + pow(adjacente, 2))

print('O comprimento da hipotenusa formado pelos catetos de comprimento {} e {} é de {}'.format(
    oposto, adjacente, hipotenusa
))
