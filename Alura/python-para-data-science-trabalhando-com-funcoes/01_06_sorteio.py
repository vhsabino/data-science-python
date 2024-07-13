'''
Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quanti-
dade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devol-
va para ela o número sorteado.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

from random import randrange

qtd = int(input("Informe a quantidade de pessoas: "))
sorteio = randrange(qtd)

print(f"Número sorteado: {sorteio}")