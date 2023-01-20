# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite um valor em metros para ser convertido: '))
centM = metros * 100
miliM = metros * 1000
print('{:.2f}m equivale a {:.2f}cm ou {:.2f}mm'.format(metros, centM, miliM))
