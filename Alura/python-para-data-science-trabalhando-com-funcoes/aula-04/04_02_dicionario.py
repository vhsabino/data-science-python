'''
Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser 
pesquisada no seguinte dicionário: 

idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, 

armazenando o resultado do valor em uma variável. O código deve conter um tratamento de 
erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e im-
primir o valor caso não ocorra nenhum.

Teste o programa com um nome presente em uma das chaves do dicionário e com um que não 
esteja no dicionário para verificar a mensagem de erro.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 21/07/2024
'''

idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nome = str(input("Digite um nome: "))
    idade = idades[nome]
    print(f"A idade de {nome} é {idade}.")
except KeyError:
    print("Erro: Nome não encontrado") 