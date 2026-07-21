"""
Exercício 2 — Removendo números repetidos

Crie a lista:

numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

Utilize Set Comprehension para criar um conjunto chamado:

sem_repeticao

Resultado esperado:

{1, 2, 3, 4, 5, 6}
"""

numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

sem_repeticao = {numero for numero in numeros}

print(sem_repeticao)