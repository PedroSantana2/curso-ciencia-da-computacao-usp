'''
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
'''

numero = int(input('Digite um numero: '))
if (numero / 2 > 1 and numero % 2 == 0) or (numero / 3 > 1 and numero % 3 == 0) or(numero / 5 > 1 and numero % 5 == 0) or numero == 1 or numero == 0 :
    print('não primo')
else:
    print('primo')
