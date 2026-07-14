"""
1.Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
"""
lista = []

while len(lista) < 6:
    valor: int = int(input(f"Informe o valor {len(lista) + 1}/6:"))
    lista.append(valor)


for valor in lista:
    print(valor)
