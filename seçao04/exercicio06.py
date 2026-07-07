"""Exercício 3

Faça um programa que leia um número inteiro.

Se o número for positivo e par, imprima:
Número positivo e par.
Se o número for positivo e ímpar, imprima:
Número positivo e ímpar.
Caso contrário, imprima:
Número negativo.
"""

numero = int(input("Digite um numero inteiro."))


if numero > 0 and numero % 2 == 0 :
    print("Numero positivo e par.")
elif numero > 0 and numero % 2 != 0:
    print("Numero positivo e impar")
else:
    print("Numero negativo")