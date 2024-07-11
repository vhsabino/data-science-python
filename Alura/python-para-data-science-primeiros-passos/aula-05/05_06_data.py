'''
Escreva um programa que peça uma data informando o dia, mês e ano 
e determine se ela é válida para uma análise.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 10/07/2024
'''

dia = int(input('digite o dia: '))
mes = int(input('digite o mes: '))
ano = int(input('digite o ano: '))

if ano < 0:
    print('ano inválido')
elif not(1 <= mes <= 12):
    print('mes inválido')
elif not(1 <= dia <= 31):
    print('dia inválido')
else:
    print('data válida')
# modificar para ano bissexto e meses com 30 dias