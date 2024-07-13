'''
Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jar-
dins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuá-
ria o raio da área circular e devolva o valor em reais do quanto precisará pagar.

Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um cír-
culo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from math import pow
from math import pi

r = float(input("Informe o raio do jardim: "))
area = pi * pow(r,2)

print(f"Preço total: R$ {round(area * 25,2)}")
