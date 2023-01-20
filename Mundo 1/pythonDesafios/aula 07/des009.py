# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print('{:=^20}'.format('TABUADA'))
numero = int(input('Digite um numero: '))

for i in range(10):
    print('{} x {} = {}'.format(numero, i+1, numero * (i+1)))
