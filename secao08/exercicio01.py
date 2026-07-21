"""
Exercício — Relatório de Notas

Crie a lista:

notas = [8, 5, 9, 10, 6, 5, 8, 7, 10]
A) List Comprehension

Crie uma lista chamada:

aprovados

Ela deve conter apenas as notas maiores ou iguais a 7.

Resultado esperado:

[8, 9, 10, 8, 7, 10]
B) Set Comprehension

Crie um conjunto chamado:

notas_unicas

Ele deve conter apenas as notas sem repetição.

Resultado esperado (a ordem pode variar):

{5, 6, 7, 8, 9, 10}
C) Dictionary Comprehension

Crie um dicionário chamado:

situacao

Onde:

a chave será a nota;
o valor será:
"Aprovado" se a nota for maior ou igual a 7;
"Reprovado" caso contrário.

Resultado esperado:

{
    5: "Reprovado",
    6: "Reprovado",
    7: "Aprovado",
    8: "Aprovado",
    9: "Aprovado",
    10: "Aprovado"
}

💡 Desafio (vale bastante a pena):

Faça a parte C utilizando o conjunto criado na parte B, ou seja, use notas_unicas em vez da lista original. Assim você evita criar chaves repetidas e pratica reutilizar estruturas que você mesmo criou.

Esse exercício reúne praticamente tudo o que você viu na Seção 8.
"""

notas = [8, 5, 9, 10, 6, 5, 8, 7, 10]

aprovados = [numeros for numeros in notas if numeros >= 7]

print(aprovados)

notas_unicas = {numero for numero in notas}

print(notas_unicas)

situacao = {
    numero: 
        "Aprovado" if numero >= 7 else "Reprovado"
    
    for numero in notas_unicas
}

print(situacao)
