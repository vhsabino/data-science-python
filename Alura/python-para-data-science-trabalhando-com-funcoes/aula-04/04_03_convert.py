'''
Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista 
para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e 
retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula 
finally para imprimir o texto: 'Fim da execução da função'.

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 21/07/2024
'''

def convert(lista: list):
    try:
        lista_new = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e),f'Erro: {e}')
    finally:
        print("Fim da execução da função")
    return lista_new

teste = [1,2,3]
teste = convert(teste)
print(teste)