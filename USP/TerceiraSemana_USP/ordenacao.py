'''
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente
'''
count = 1
anterior = 0

while count <= 3 :
    numero = int(input('Digite um número: '))
    if count > 2 :
        resultado = 'não está em ordem crescente'
        if numero > anterior :
            resultado = 'crescente'
    anterior = numero
    count += 1
print(resultado)
