'''
Desenvolva um programa que leia um conjunto indeterminado de temperaturas 
em Celsius e informe a média delas. A leitura deve ser encerrada ao ser 
enviado o valor -273°C.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

temperatura = 0
soma = 0
qtd = 0
while True:
    temperatura = float(input('digite uma temperatura: '))
    if temperatura == -273.0:
        break
    soma += temperatura
    qtd += 1
media = soma / qtd
print(f'A média de temperaturas eh: {media}')