'''
Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a esco-
lha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguin-
te formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

def tabuada(numero: int):
    print(f'Tabuada do {numero}')
    for i in range (1,11):
        print(f'{numero} x {i} = {numero*i}')

numero = int(input('digite um número: '))
tabuada(numero)