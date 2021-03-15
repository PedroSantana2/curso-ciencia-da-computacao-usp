'''
Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.
'''
n = int(input("Digite um número inteiro: "))
count = 1 
n_fat = 1  
while count <= n:
    n_fat = n_fat * count
    count += 1
print(n_fat)   
