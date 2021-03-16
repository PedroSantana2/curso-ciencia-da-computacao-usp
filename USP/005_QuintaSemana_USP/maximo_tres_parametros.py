'''
Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
'''

def maximo(x, y, z) :
    if x > y and x > z :
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return x
        