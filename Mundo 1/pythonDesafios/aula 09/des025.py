# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome: ')

temSilva = 'SILVA' in nome.upper()
print(temSilva)
print('A pessoa com nome', '"'+nome+'"', '' if temSilva else 'não', 'tem silva no nome')
