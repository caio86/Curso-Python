frase = str(input('Digite uma frase: ')).upper().strip()

qtdLetraA = frase.count('A')
primeiraA = frase.find('A') + 1
ultimaA = frase.rfind('A') + 1

print('A letra A aparece {} vezes na frase.'.format(qtdLetraA))
print('A primeira letra A apareceu na posição {}'.format(primeiraA))
print('A última letra A apareceu na posição {}'.format(ultimaA))
