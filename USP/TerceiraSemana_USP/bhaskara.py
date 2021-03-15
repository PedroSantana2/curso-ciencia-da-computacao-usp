'''
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros  a a,  b b, e  c c da equação  ax^2 + bx + c ax 
2
 +bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou

a raiz dupla desta equação é X

onde X é o valor da raiz dupla

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0

Como enviar
Quando você estiver pronto para enviar, você pode fazer upload dos arquivos para cada parte da tarefa na guia "Meu envio".
'''
from math import sqrt
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = b ** 2 - (4 * a * c)

if delta < 0 :
    print('esta equação não possui raízes reais')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    if delta == 0 :
        print('a raiz dupla desta equação é {}'.format())
    else:
        if x1 > x2 :
            print('as raízes da equação são {} e {}'.format(x1, x2))
        else:
            print('as raízes da equação são {} e {}'.format(x2, x1))
    