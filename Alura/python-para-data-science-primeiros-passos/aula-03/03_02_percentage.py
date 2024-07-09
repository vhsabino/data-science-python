'''
Escreva um programa que solicite o percentual de crescimento 
de produção de uma empresa e informe se houve um crescimento 
(porcentagem positiva) ou decrescimento (porcentagem negativa).

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

percentual = float(input('digite o percentual de crescimento de uma empresa: '))

if (percentual >= 0.0):
    print('houve um crescimento')
else:
    print('houve um decrescimento')