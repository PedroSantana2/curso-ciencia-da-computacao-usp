'''
Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.
Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"
Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.
Seu Programa
Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.
Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho funcione corretamente.
O programa deve implementar:
Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.
Uma função usuário_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.
Cuidado: o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as funções do jogo (a menos que essa chamada esteja dentro de uma função). Se seu programa usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.
Campeonatos
Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma
Placar: Você ??? X ??? Computador
Execução
Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar apenas uma partida (opção 1) ou um campeonato (opção 2).
Atenção: o corretor automático vai verificar se você está utilizando exatamente as mensagens pedidas, como "Você começa!", "O computador ganhou!" etc. Deixe para usar a sua criatividade em outros lugares!
'''

import sys, random
#Definindo funções:

# p = peças totais | mr = maior_retirada

#Calcula qual será a quantidade de peças que o computador jogará de acordo com o enunciado:
def computador_escolhe_jogada(p, mr):
    resposta = random.randint(1, mr)
    return resposta

#Recebe a quantidade de peças se1lecionadas pelo jogador:
def usuario_escolhe_jogada(p, mr):
    valor = int(input('\n\t[ ? ] Quantas peças você vai tirar\n=> '))

    #Mensagem de erro para valores não aceitos:
    while valor <= 0 or valor > mr or valor > p:
        print('\n\t[ ⚠ ] Oops! Jogada inválida! Tente de novo.')
        valor = int(input('\t[ ? ] Quantas peças você vai tirar\n=> '))

    #Caso esteja tudo certo, a função devolve o valor determinado pelo usuário:
    return valor

#Função para controlar o jogo:
def partida():
    autenticaçao = True
    while autenticaçao:
        #Recebendo informações do usuário:
        p = int(input('\n\t[ ? ] Quantidade de peças\n=> '))
        mr = int(input('\n\t[ ? ] Limite de peças por jogada\n=> '))
        if (p == 0) or (mr == 0):
            print('\n\t[ ⚠ ] Informações ínvalidas! Tente novamente.')
        else:
            autenticaçao = False

    #Conferindo se as informações são válidas:
    while mr < 1:
        print('\n\t[ ⚠ ] A quantidade de peças por jogadas devem ser menor ou igual as peças totais.')
        mr = int(input('\n\t[ ? ] Limite de peças por jogada\n=> '))
        
    #Calculando quem começará primeiro:
    quem_inicia = random.randint(1, 2)
    if quem_inicia == 1:
        print('\t[ 😎 ] Você começa!')

        # 1 = vez do usuário, 2 = vez do computador
        jogada = 1

        #Conferindo se ainda existe peças:
        while p > 0:

            if jogada == 1 :
                result = usuario_escolhe_jogada(p, mr)
                print('\n\t[ ! ] Você tirou', result, 'peça(s).')

                #Retirando a quantidade escolhida pelo usuário do todo:
                p = p - result
                print('\t[ ! ] Agora restam', p, 'peças no tabuleiro.')

                #Alternando para iniciar a vez do computador
                jogada = 2

            else:
                result = computador_escolhe_jogada(p, mr)
                print('\n\t[ ! ] O computador tirou', result, 'peça(s)')

                #Retirando a quantidade escolhida pelo computador do todo:
                p = p - result
                print('\t[ ! ] Agora restam', p, 'peças no tabuleiro.')

                #Alternando para iniciar a vez do usuário:
                jogada = 1

        #Confere quem jogou por último e ganhou a partida:
        if jogada == 1:
            print('\n\t[ 💻 ] Fim do jogo! O computador ganhou!\n')

            #Ponto do computador (Usado no campeonato):
            return 2 

        else:
            print('\n\t[ 😎 ] Fim do jogo! O você ganhou!\n')

            #Ponto do jogador (Usado no campeonato):
            return 1 

    else:
        print('\n\t[ ⚙ ] Computador começa!')

        # 1 = vez do usuário, 2 = vez do computador
        jogada = 2

        #Conferindo se ainda existe peças:
        while p > 0:

            if jogada == 2:
                result = computador_escolhe_jogada(p, mr)
                print('\n\t[ ! ] O computador tirou', result, 'peça(s).')

                #Retirando a quantidade escolhida pelo computador do todo:
                p = p - result
                print('\t[ ! ] Agora restam', p, 'peças no tabuleiro.')

                #Alternando para iniciar a vez do usuário:
                jogada = 1

            else:
                result = usuario_escolhe_jogada(p, mr)
                print('\n\t[ ! ] Você tirou', result, 'peça(s).')

                #Retirando a quantidade escolhida pelo usuário do todo:
                p = p - result
                print('\t[ ! ] Agora restam', p, 'peças no tabuleiro.\n')

                #Alternando para iniciar a vez do computador:
                jogada = 2

        if jogada == 1:
            print('\n\t[ 💻 ] Fim do jogo! O computador ganhou!')

            #Ponto do computador (Usado no campeonato):
            return 2

        else:
            print('\n\t[ 😎 ]Fim do jogo! O você ganhou!')

            #Ponto do jogador (Usado no campeonato):
            return 1 

def campeonato():
    #Contador de partidas:
    partidas = 1

    #Pontos do computador e do usuário:
    pts_pc = pts_user = 0

    #Limitador para acontecerem apenas 3 partidas:
    while partidas < 4:
        print('\n\t[ ⌛ ] Rodada', partidas)

        #Caso o valor da partida retorne 1, significa que o usuário ganhou:
        if partida() == 1:
            pts_user = pts_user + 1

        #Caso contrário, significa que o computador venceu:
        else:
            pts_pc = pts_pc + 1

        #Contador aumenta em 1 a cada partida:
        partidas = partidas + 1

    #Resultados:
    print('\t[ 🥇 ] Final do campeonato!')
    print('\t[ 🥇 ] Placar: Você', pts_user, 'X', pts_pc, 'Computador')

#Função para mostrar mensagem no final:
def fim() :

    #Loop até ser receber uma resposta valida:
    while True:
        print('\n\tDeseja iniciar outra partida?\n\t[ 1 ] Sim.\n\t[ 2 ] Não.\n')
        resposta = int(input('=> '))

        #Se sim, o jogo será iniciado novamente:
        if resposta == 1:
            jogo_completo()

        #Se não, o jogo será fechado:
        elif resposta == 2:
            sys.exit()

        #Mensagem para resposta ínvalida:
        else:
            print('[ ⚠ ] Resposta ínvalida!')

#Função principal:
def jogo_completo() :

    #Loop até receber uma mensagem valida:
    while True :
        print('\n\tBem-vindo ao jogo do NIM! Escolha:\n')
        print('\t[ 1 ] Para jogar uma partida isolada.\n\t[ 2 ] Para jogar um campeonato.')
        resposta = int(input('=> '))

        if resposta == 1 :
            partida()
            fim()

        elif resposta == 2 :
            campeonato()
            fim()

        else:
            print('\n\t[ ⚠ ] Resposta ínvalida! Tente novamente.')

#Iniciando jogo:
jogo_completo()
