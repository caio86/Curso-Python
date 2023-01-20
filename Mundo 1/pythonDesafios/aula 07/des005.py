# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
numero = int(input('Digite um número: '))
print('O número digitado foi: {}\no seu sucessor é: {}\ne o seu antecessor é: {}'.format(
    numero, numero+1, numero-1)
)
