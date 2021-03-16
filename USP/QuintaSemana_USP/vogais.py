'''
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
'''
def vogal(x) :
    x = x.upper()
    if (x == 'A') or (x == 'E') or (x == 'I') or (x == 'O') or (x == 'U'):
        return True
    else:
        return False
