'''
Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em 
seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 
3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código 
que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from random import choice

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada = []
for i in range(0,3):
    salada.append(choice(frutas))

print(salada)