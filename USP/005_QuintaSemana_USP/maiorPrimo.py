'''
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
'''
def maior_primo(x) :
    if x > 1 :
        while 1 > 0 :
            if not((x / 2 > 1 and x % 2 == 0) or (x / 3 > 1 and x % 3 == 0) or(x / 5 > 1 and x % 5 == 0)) :
                return x
                break
            x = x - 1
    else:
        return 'Número ínvalido'
