'''
Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontua-
ções de estudantes de uma instituição de ensino de acordo com suas respostas num teste. 
Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em 
que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada ques-
tão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você 
deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de 
alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as 
alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida 
uma lista com as notas em cada teste.

Os dados para o teste do código são:

Gabarito da prova:

gabarito = ['D', 'A', 'B', 'C', 'A']

Abaixo temos 2 listas de listas que você pode usar como teste

Notas sem exceção:

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

Notas com exceção:

testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estru-
tura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.


Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 21/07/2024
'''

def nota(respostas: list, gabarito: list):
    notas = []
    j = 0
    try:
        for resposta in respostas:
            nota = 0
            for i in range(len(gabarito)):
                if resposta[i] not in ['A','B','C','D']:
                    raise ValueError(f"A alternativa {resposta[i]} não é uma opção de alternativa válida")
                if resposta[i] == gabarito[i]:
                    nota += 1
            notas.append(nota)
    except Exception as e:
        print(e)
    return notas

gabarito = ['D', 'A', 'B', 'C', 'A']
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

resultado_1 = nota(testes_sem_ex, gabarito)
print(resultado_1)

resultado_2 = nota(testes_com_ex, gabarito)
print(resultado_2)