'''
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
'''

#Definindo função:
def remove_repetidos(lista):

    #Criando lista pare receber o valor da lista sem as repetições:
    lista_sem_repetir = []

    #Comando para percorrer toda a lista:
    for i in lista:

        #Caso o item não esteja na lista criada "lista_sem_repetir" será adicionada em tal:
        if i not in lista_sem_repetir:

            #Adicionando item que não estava na lista:
            lista_sem_repetir.append(i)
    
    #Comando para organizar a lista em ordem crescente:
    lista_sem_repetir.sort()
    return lista_sem_repetir
