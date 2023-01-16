# Faça um programa que leia três números e mostre qual pe o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
maior = n1

n2 = int(input('Digite o segundo número: '))
if n2 > maior: maior = n2

n3 = int(input('Digite o terceiro número: '))
if n3 > maior: maior = n3

print('O número maior foi {}'.format(maior))
