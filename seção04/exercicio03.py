#3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

num1 = int(input("escreva o primeiro numero:"))
num2 = int(input("escreva o segundo numero:"))
num3 = int(input("escreva o terceiro numero:"))
q1 = num1 * num1
q2 = num2 * num2
q3 = num3 * num3
somaq = q1 + q2 + q3
print(f"A soma dos quadrados desses numeros é de {somaq}")
