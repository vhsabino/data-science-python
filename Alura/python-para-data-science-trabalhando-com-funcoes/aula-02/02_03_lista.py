'''
Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 13/07/2024
'''

def multiplos_de_3(lista: list):
    nova_lista = []
    for elemento in lista:
        if elemento % 3 == 0:
            nova_lista.append(elemento)
    return nova_lista

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = multiplos_de_3(lista)
print(f"Multiplos de 3: {mult_3}")