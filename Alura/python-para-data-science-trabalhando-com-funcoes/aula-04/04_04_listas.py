'''
Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um 
das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo 
elemento da tupla são os valores na posição i das listas e o terceiro elemento é a so-
ma dos valores na posição i das listas.

A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar 
como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tama-
nhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de 
elementos em cada lista é diferente.' Dados para testar a função:

Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]

Listas com tamanhos diferentes:
lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]

Listas com valores incoerentes:
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 21/07/2024
'''

def formar_tuplas(lista_a: list, lista_b: list):
    if len(lista_a) != len(lista_b):
        raise IndexError("A quantidade de elementos em cada lista é diferente.")
    try:
        lista_completa = [(lista_a[i], lista_b[i], lista_a[i] + lista_b[i]) for i in range(len(lista1))]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    return lista_completa

lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]

lista3 = formar_tuplas(lista1, lista2)
print(lista3)