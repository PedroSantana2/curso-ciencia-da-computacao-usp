'''
Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
'''
quantidade = int(input('Digite a quantidade de numeros ímpares: '))
contador = 1
numero = 1
while contador <= quantidade :
    if numero % 2 != 0 :
        print(numero)
        contador = contador + 1
    numero = numero + 1
