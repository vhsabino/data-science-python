
import matplotlib.pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# podemos fazer múltiplas chamadas para plt.plot
# para mostrar múltiplas séries no mesmo gráfico
plt.plot(xs, variance, 'g-', label='variance') # linha verde sólida
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # linha com linha de ponto tracejado vermelho
plt.plot(xs, total_error, 'b:', label='total error') # linha com pontilhado azul

# porque atribuímos rótulos para cada série
# podemos obter uma legenda gratuita
# loc=9 significa “top center”
plt.legend(loc=9)
plt.xlabel("complexidade do modelo")
plt.title("Compromisso entre Polarização e Variância")
plt.show()

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)

# nomeia cada posição
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count), # coloca o rótulo com sua posição
        xytext=(5, -5), # mas compensa um pouco
        textcoords='offset points')
plt.title("Minutos Diários vs. Número de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("minutos diários passados no site")
plt.show()

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades, test_2_grades)
plt.title("Os eixos são compatíveis")
plt.xlabel("nota do teste 2") 
plt.ylabel("nota do teste 1")
plt.axis('equal')
plt.show()