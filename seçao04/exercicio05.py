"""Faça um programa que leia:

um nome;
uma idade.

Se a pessoa tiver 18 anos ou mais e o nome não estiver vazio, imprima:

Cadastro realizado com sucesso.

Caso contrário, imprima:

Cadastro inválido.
"""
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18 and nome != "":
    print("Cadastro realizado com sucesso")
else:
    print("Cadastro inválido")
    
    