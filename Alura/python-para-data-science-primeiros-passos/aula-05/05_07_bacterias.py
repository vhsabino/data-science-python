'''
Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o 
número de bactérias por dia (em milhares) e pode ser observado a seguir: 

[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. 

Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de
bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do
dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 

100 * (amostra_atual - amostra_passada) / (amostra_passada).

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

lista = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

amostra_prev = 1
percentual = []

for amostra in lista:
    percentual.append(100 * (amostra - amostra_prev) / (amostra_prev))
    amostra_prev = amostra
print(percentual)