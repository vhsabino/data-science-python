'''
Em uma eleição para gerência em uma empresa com 20 pessoas 
colaboradoras, existem quatro candidatos(as). Escreva um 
programa que calcule o(a) vencedor(a) da eleição. A votação 
ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas 
(que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo 
número 5) e os votos em branco (representados pelo número 6).
Ao final da votação, o programa deve exibir o número total de 
votos para cada candidato(a), os nulos e os votos em branco. 
Além disso, deve calcular e exibir a porcentagem de votos nulos 
em relação ao total de votos e a porcentagem de votos em branco 
em relação ao total de votos.



Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''
votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
votos_nulo = 0
votos_branco = 0
for i in range(1,21):
    voto = int(input('digite seu voto: '))
    if voto == 1:
        votos_1 += 1
    elif voto == 2:
        votos_2 += 1
    elif voto == 3:
        votos_3 += 1
    elif voto == 4:
        votos_4 += 1
    elif voto == 5:
        votos_nulo += 1
    elif voto == 6:
        votos_branco += 1

print(f'Candidato 1: {votos_1} votos.')
print(f'Candidato 2: {votos_2} votos.')
print(f'Candidato 3: {votos_3} votos.')
print(f'Candidato 4: {votos_4} votos.')
print(f'Nulos: {votos_nulo} votos.')
print(f'Brancos: {votos_branco} votos.')
print(f'Nulos: {(votos_nulo / 20) * 100}%')
print(f'Brancos: {(votos_branco / 20) * 100}%')