'''
Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
'''

lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero > 0:
        lista.append(numero)
        continue
    else:
        break
a = -1
for i in lista:
    print(lista[a])
    a = a - 1
