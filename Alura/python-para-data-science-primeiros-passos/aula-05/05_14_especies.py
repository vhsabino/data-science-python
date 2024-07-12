'''
Uma equipe de cientistas de dados está estudando a diversidade biológica em uma 
floresta. A equipe fez a coleta de informações sobre o número de espécies de plan-
tas e animais em cada área dessa floresta e armazenou essas informações em um dicio-
nário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem 
às espécies de plantas e animais nas áreas, respectivamente.

{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

Escreva um código para calcular a média de espécies por área e identificar a área 3
com a maior diversidade biológica. Dica: use as funções built-in sum() e len().

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 12/07/2024
'''

floresta = {'Área Norte': [2819, 7236],
            'Área Leste': [1440, 9492],
            'Área Sul': [5969, 7496],
            'Área Oeste': [14446, 49688],
            'Área Centro': [22558, 45148]}

maior_especie = 0
maior_area = ''
for area, especies in floresta.items():
    media = sum(especies) / len(especies)
    if media > maior_especie:
        maior_especie = media
        maior_area = area

print(f'Área com maior diversidade biológica: {maior_area}')