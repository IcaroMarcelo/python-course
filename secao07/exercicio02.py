"""
2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 2024”.
"""

def data_por_extenso(data):
    data = data.split("/")
    dia,mes,ano = data
    meses = {
        "01" : "Janeiro",
        "02" : "Fevereiro",
        "03" : "Março",
        "04" : "Abril",
        "05" : "Maio",
        "06" : "Junho",
        "07" : "Julho",
        "08" : "Agosto",
        "09" : "Setembro",
        "10" : "Outubro",
        "11" : "Novembro",
        "12" : "Dezembro"
    }
    nome_mes = meses[mes]
    dia = int(dia)
    print(f"{dia} de {nome_mes} de {ano}")
    
data_por_extenso("02/06/2024")