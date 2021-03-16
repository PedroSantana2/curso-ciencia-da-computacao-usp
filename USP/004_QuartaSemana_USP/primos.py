'''
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
'''

numero = int(input("Digite um número: "))
count = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        count += 1
        print(i)
        print(count)
if count == 2:
    print("primo")
else:
    print("não primo")