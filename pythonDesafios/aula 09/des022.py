# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaçõs).
# Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome: ')
print('Nome Maiúsculo:', nome.upper())
print('Nome Minúsculo:', nome.lower())
print('O seu nome tem', len(nome.replace(' ', '')) ,'letras')
print('O seu primeiro nome tem', len(nome.split()[0]) ,'letras')
