'''
Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias 
de um serviço da empresa, precisamos verificar se as notas são válidas. 
Então, escreva um programa que vai receber a nota de 0 a 5 de todos os 
dados e verificar se é um valor válido. Caso seja inserido uma nota acima 
de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

for i in range(1,16):
    nota = -1
    while (nota < 0) or (nota > 5):
        nota = int(input('avalie o serviço da empresa de 0 a 5: '))
    print('Obrigado!')
print('fim.')