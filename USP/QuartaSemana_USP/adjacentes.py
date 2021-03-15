'''
Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
'''

numero = input('Digite um numero: ')
len = len(numero)
x = 10
y = 1
valor = 0
valor_anterior = -1
resultado = 'não'
numero = int(numero)
contador = 1
while contador <= len :
    valor = numero % x // y
    x = x * 10
    y = y * 10
    if valor == valor_anterior :
        resultado = 'sim'
        break
    valor_anterior = valor
    contador = contador + 1
print(resultado)
