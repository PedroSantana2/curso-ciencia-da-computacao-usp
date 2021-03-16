'''
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
'''
def n_primos(numero):
    count = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            count += 1
    if count == 2:
        print(numero)
        return 1

numero = int(input('Digite um número e tenha a quantidade de primos até ele: '))
print('Primos: ')
primos = 0
while numero > 0:
    if n_primos(numero) == 1:
        primos = primos + 1
    numero = numero - 1
print('\nResultado: ')
print(primos)