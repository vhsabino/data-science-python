'''
Escreva um programa que pergunte em qual turno a pessoa usuária 
estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!",
 "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

Curso: Python para Data Science: primeiros passos
Autor: Victor Sabino
Data: 09/07/2024
'''

turno = str(input('Qual turno vc estuda? '))

if (turno == 'manhã'):
    print('Bom Dia!')
elif(turno == 'tarde'):
    print('Boa Tarde!')
elif(turno == 'noite'):
    print('Boa Noite!')
else:
    print('Valor Inválido!')