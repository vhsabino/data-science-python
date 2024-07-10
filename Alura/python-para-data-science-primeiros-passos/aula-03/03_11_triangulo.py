'''
Escreva um programa que peça à pessoa usuária três números 
que representam os lados de um triângulo. O programa deve 
informar se os valores podem ser utilizados para formar um 
triângulo e, caso afirmativo, se ele é equilátero, isósceles 
ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois 
lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

lado_1 = float(input('digite valor do primeiro lado: '))
lado_2 = float(input('digite valor do segundo lado: '))
lado_3 = float(input('digite valor do terceiro lado: '))

if (lado_1 + lado_2) > lado_3:
    if (lado_1 == lado_2 == lado_3):
        print('eh um triângulo equilátero')
    elif (lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
        print('eh um triângulo isósceles')
    else:
        print('eh um triângulo escaleno')
else:
    print('não é um triângulo.')