 #* Começa com "\033[" termina com "m" e entre os dois vai os códigos
 # são 3 códigos o código de estilo, o código de texto e o código de fundo, eles são divididos por ":"
# Exemplo: \033[0:33:44m

# Estilo:
# 0: None, 1: Bold, 4: Underline, 7: Negative

# Cores Texto:
# 30: Preto, 31: Vermelho, 32: Verde, 33: Amarelo, 34: Azul, 35: Magenta, 36: Ciano, 37 Cinza, 97: Branco

# Cores Backgorund:
# 40: Preto, 41: Vermelho, 32: verde, 33: Amarelo, 34: Azul, 35: Magenta, 36: Ciano, 47: Cinza, 107: Branco

a = 3
b = 5

print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a, b))

nome = 'Guanabara'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7:97m'
}
print('Olá, Muito prazer em te conhecer, {1}{0}{2}!!!'.format(nome, cores['pretoebranco'], cores['limpa']))




