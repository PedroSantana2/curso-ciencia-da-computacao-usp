'''
Receba um número inteiro na entrada e imprima

 par 

quando o número for par ou

ímpar

quando o número for ímpar.
'''

numero = int(input('Digite um número: '))
resultado = 'ímpar'
if numero % 2 == 0 or numero == 0 :
    resultado = 'par'
print(resultado)
