'''
Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar 
as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar
 um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 
 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontua-
ção dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresen-
tar o texto:

"Nota da manobra: [media]"

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 14/07/2024
'''

def remove_max(lista: list):
    lista.remove(max(lista))
    return lista

def remove_min(lista: list):
    lista.remove(min(lista))
    return lista

lista = []
for i in range(0,5):
    nota = float(input(f"informe a nota {i}: "))
    lista.append(nota)

lista = remove_max(lista)
lista = remove_min(lista)

print(f'Nota da manobra: {sum(lista) / len(lista)}')
