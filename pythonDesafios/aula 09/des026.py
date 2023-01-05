# faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')

qtdLetraA = frase.upper().count('A')
primeiraA = frase.upper().find('A')
ultimaA = frase.upper().rfind('A')

print('Na frase:', frase)
print('A letra "A" aparece', qtdLetraA, 'vezes')
print('A primeira vez que ela aparece é na posição:', primeiraA)
print('A última vez que ela aparece é na posição:', ultimaA)
