'''
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
'''
numero = input('Digite um numero: ')
len = len(numero)
x, y, valor = 10, 1, 0 
numero = int(numero)
contador = 1
while contador <= len :
    valor = valor + (numero % x // y)
    x = x * 10
    y = y * 10
    contador = contador + 1
print(valor)
