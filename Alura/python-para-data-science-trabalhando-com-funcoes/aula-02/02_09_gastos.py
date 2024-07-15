'''
Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das 
quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem 
de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com 
passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], 
respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente 
[850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com 
hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos 
com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. 
Considere a viagem de ida e volta de carro.

"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de 
Recife custaria [gastos] reais"

Curso: Python para Data Science: trabalhando com funções, estruturas de dados e exceções
Autor: Victor Sabino
Data: 14/07/2024
'''

diaria = 150 #reais
consumo = 14 #km/litro
gasolina = 5 #r$/litro
alimentacao = [200, 400, 250, 300] #reais/dia
distancia = [850, 800, 300, 550] #km entre recife e as cidades
cidades = ["Salvador", "Fortaleza", "Natal", "Aracaju"]

def gasto_hotel(destino: str, dias: int):
    pos = cidades.index(destino)
    comida = alimentacao[pos] * dias
    hotel_total = comida + diaria * dias
    return hotel_total

def gasto_gasolina(destino: str):
    pos = cidades.index(destino)
    gasolina_total = distancia[pos] * 2 * gasolina / consumo
    return gasolina_total

def gasto_passeio(destino: str, dias: int):
    combustivel = gasto_gasolina(destino)
    hotel = gasto_hotel(destino,dias)
    gasto_total = combustivel + hotel
    return gasto_total

destino = str(input("Qual o destino? "))
dias = int(input("Quantos dias vc vai passar em {destino}? "))
gastos = gasto_passeio(destino,dias)

print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {destino} saindo de Recife custaria {round(gastos,2)} reais")