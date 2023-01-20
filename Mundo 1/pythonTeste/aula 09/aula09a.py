frase = "Curso em Vídeo Python"
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:])
print(frase[:5])
print(frase[9::2])
print(frase[9::3])

print('\nAnálise\n')

print('len(frase) =', len(frase))
print('frase.count("o") =', frase.count('o'))
print("frase.find('deo') =", frase.find('deo'))
print("frase.find('Android') =", frase.find('Android'))
print("'Curso' in frase =", 'Curso' in frase)

print('\nTransformação\n')

print("frase.replace('Python', 'Android') =", frase.replace('Python', 'Android'))
print("frase.upper() =", frase.upper())
print("frase.lower() =", frase.lower())
print("frase.capitalize() =", frase.capitalize())
print("frase.title() =", frase.title())

frase = '   Aprenda Python  '
print('\n'+frase)

print("frase.strip() =", frase.strip())  # Remove espaços a mais na string
print("frase.rstrip() =", frase.rstrip()) # Remove os espaços a direita da string
print("frase.lstrip() =", frase.lstrip()) # Remove os espaços a esquerda da string

frase = "Curso em Video Python"
print('\nDivisão\n')

print("frase.split() =", frase.split())
print("'-'.join(frase.split()) =", '-'.join(frase.split()))
dividido = frase.split()
print(dividido)
print(dividido[2][3])
