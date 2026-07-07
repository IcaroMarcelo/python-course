"""Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

num1 = int(input(f"Digite um numero: "))

if num1 >= 0:
    raiz = num1 ** 0.5
    print(f"A raiz quadrada deste numero é de {raiz}")
else: print(f"numero inválido.")
    
