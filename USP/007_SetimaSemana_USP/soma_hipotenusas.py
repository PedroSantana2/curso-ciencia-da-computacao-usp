'''
Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, nn é uma hipotenusa se existem números inteiros ii e jj tais que:

 n^2 = i^2 + j^2 n 2=i 2+j 2
 

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo  n n e devolva a soma de todos os inteiros entre 1 e  n n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até  n n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.
'''
def calcular_hipotenusa(a, b):
    #Calculando Hipotenusa de acordo com os valores recebidos:
    return a ** 2 + b ** 2

def soma_hipotenusas(n):
    c = 1
    soma = 0

    while c <= n:

        c2 = c ** 2    
        a = 1
        b = 1
    
        while a < n:

            while b < n:

                if (c2 == calcular_hipotenusa(a, b)):
                    soma = soma + c
                    a = n
                    break

                b += 1

            a += 1
            b = a

        c += 1
  
    return soma

n = int(input('Digite um número: '))
print(soma_hipotenusas(n))
