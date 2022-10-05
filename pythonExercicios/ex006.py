# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQ = pow(numero, (1/2))

print('Numero digitado: {}'.format(numero))
print('O dobro de {0} é: {1}\nO triplo de {0} é: {2}\nA raiz quadrada de {0} é: {3:.2f}'.format(
    numero, dobro, triplo, raizQ
))

