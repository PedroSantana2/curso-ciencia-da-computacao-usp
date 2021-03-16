'''
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto
'''
from math import sqrt
x1 = int(input('Digite o valor do x1: '))
y1 = int(input('Digite o valor do y1: '))
x2 = int(input('Digite o valor do x2: '))
y2 = int(input('Digite o valor do y2: '))
distancia = sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)
resposta = 'perto'
if distancia >= 10 :
    resposta = 'longe'
print(resposta)