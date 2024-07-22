'''
Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório 
que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório pre-
cisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura 
do ambiente controlado recolhidos durante a experimentação para definir a melhor condi-
ção para os testes.

Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os 
dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma 
nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e 
você deve tratar dentro dela ao menos 2 tipos de exceções:

Verificar se as listas têm o mesmo tamanho (ValueError)
Verificar se existe alguma divisão por zero (ZeroDivisionError)
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no 
experimento, com os valores de pressão e temperatura do ambiente controlado.

Como teste, use os seguintes dados:

Dados sem exceção:

pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

Dados com exceção:
1) Exceção de ZeroDivisionError

    pressoes = [60, 120, 140, 160, 180]
    temperaturas = [0, 25, 30, 35, 40]

2) Exceção de ValueError   

    pressoes = [100, 120, 140, 160]
    temperaturas = [20, 25, 30, 35, 40]

Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estru-
tura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na 
saída.


Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 21/07/2024
'''

def divide_colunas(pressao: list, temperatura: list):
    divisao = []
    if len(pressao) != len(temperatura):
        raise ValueError("A quantidade de elementos em cada lista é diferente.")
    try:
        for i in range(len(pressao)):
            division_result = pressao[i] / temperatura[i]
            divisao.append(division_result)
    except Exception as e:
        print(e)
    return divisao

pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

resultado = divide_colunas(pressoes, temperaturas)
print(resultado)