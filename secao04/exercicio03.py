#Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

num1 = int(input("Informe um numero pra mim: "))

if num1 % 2 == 0:
    print(f"O numero é par")
else:
    print(f"O numero não é par")