'''
Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com 
suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada ques-
tão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão
vale um ponto e existem as alternativas A, B, C ou D.

Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 11/07/2024
'''

gabarito = {'questao_1' : 'D', 
            'questao_2' : 'A', 
            'questao_3' : 'C',
            'questao_4' : 'B',
            'questao_5' : 'A',
            'questao_6' : 'D',
            'questao_7' : 'C',
            'questao_8' : 'C',
            'questao_9' : 'A',
            'questao_10' : 'B'}

nota = 0
questao = 1
for respostas in gabarito.values():
    resposta = str(input(f'digite a resposta da questão {questao}: ')).upper()
    if resposta == respostas:
        nota += 1
    #print(f'Resposta: {resposta} | Gabarito: {respostas}')
    questao += 1
print(f'Nota final: {nota}')