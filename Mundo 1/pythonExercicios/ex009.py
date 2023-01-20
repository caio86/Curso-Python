# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print('{:=^20}'.format('TABUADA'))
numero = int(input('Digite um numero: '))

print('-' * 12)
for i in range(10):
    print('{} x {:2} = {}'.format(numero, i+1, numero * (i+1)))
print('-' * 12)
