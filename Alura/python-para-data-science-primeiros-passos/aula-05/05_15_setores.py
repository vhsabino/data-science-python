'''
O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) 
de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de 
idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão aci-
ma da idade média geral.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 12/07/2024
'''

setores = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
            'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
            'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
            'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

qtd_acima = 0
media_setor = 0
media_geral = 0
for setor, idades in setores.items():
    media = sum(idades) / len(idades)
    print(f'Média de idade do {setor}: {media}')
    media_geral += media
media_geral = media_geral / 4
print(f'Média de idade geral: {media_geral}')
for idades in setores.values():
    for idade in idades:
        if idade > media_geral:
            qtd_acima += 1
print(f'Qtd de pessoas acima da idade média: {qtd_acima}')