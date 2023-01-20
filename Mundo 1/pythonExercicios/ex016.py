from math import trunc

numero = float(input('Digite um número: '))
parteInteira = trunc(numero)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, parteInteira))
