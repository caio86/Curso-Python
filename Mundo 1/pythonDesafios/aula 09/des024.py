# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite um nome de uma cidade: ')

tem_santo = 'SANTO' in cidade.split()[0].upper()
print('A cidade ', '"'+cidade+'"',  '' if tem_santo else ' não' ,' começa com o nome SANTO', sep='')
