# [PY-A06] Considere o seguinte trecho de código em Python:

import random



lista = [1, 2, 3, 4, 5]

x = random.choice(lista)

# a) Explique o que o código faz:
print('a) O código importa uma biblioteca com comando para gerar números pseudo-aleatórios limitados aos números da lista, de maneira que ao rodar o \n'
      ' código, um número da lista será escolhido aleatoriamente')
print("")

# b) Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive):

print(f"b) Número aleatório entre 10 a 20 (incluídos): {random.randrange(10, 21)}")
print("")

# c) Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive):

print("c) Sequência de 5 números aleatórios entre 1 e 100 (incluídos):")
for i in range(1,6):
    print(f"  {i}: {random.randrange(1, 101)}")