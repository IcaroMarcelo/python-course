"""Faça um programa que leia a idade de uma pessoa.

Se ela tiver 18 anos ou mais, imprima:
Entrada permitida.
Caso contrário, imprima:
Entrada não permitida.
"""

idade = int(input("Digite sua idade por favor"))

if idade >= 18:
    print("Entrada permitida")
else:
    print("Entrada não permitida")