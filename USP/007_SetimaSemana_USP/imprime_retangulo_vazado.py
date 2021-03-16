'''
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
'''
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

if (largura > 2) and (altura > 2):
    meio = largura - 4
    espaços = ' ' * meio
    contador = 1
    while contador <= altura:
        if contador == 1:
            print('#' * largura)

        if altura - contador == 0:
            print('#' * largura)
            
        elif contador > 1:
            print('#',espaços, '#')
        contador += 1

else:
    contador = 1
    while contador <= altura:
        print('#' * largura)
        contador += 1
