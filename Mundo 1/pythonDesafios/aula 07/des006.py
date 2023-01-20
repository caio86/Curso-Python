# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um número: '))
print('Numero digitado: {}'.format(numero))
print('O dobro de {0} é: {1}\nO triplo de {0} é: {2}\nA raiz quadrada de {0} é: {3}'.format(
    numero, numero * 2, numero * 3, numero**(1/2)
))

