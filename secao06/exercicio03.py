"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""
lista: list[int] = []
pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f"Informe o valor {len(lista) + 1}/10:"))
    lista.append(valor)
    
    if valor % 2 == 0:
        pares = pares + 1
        
if pares > 0:
    print(f"A lista {lista} possui {pares} pares.")
else:
    print(f"A lista {lista} não possui pares.")
    
