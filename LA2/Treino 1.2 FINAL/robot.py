'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''
comandos1 = "EEAADAAAAAADAAAADDDAAAHAAAH"
comandos2 = "H"


def robot(comandos):
    #Direcao e cordenadas a 0
    direcao = 0
    x, y = 0, 0

    #Listas, sendo que a lista_posicoes começa com o (0,0) pois é a posicao inicial a registar
    lista_posicoes = [(0,0)]
    lista_final = []

    #percorrer todos os comandos
    for letra in comandos:
        # calcular a direcao
        direcao = calc_direcao(direcao, letra)

        # Se for pra avancar, ter em conta a direcao
        if letra == "A":
            # Avancar Baseado na direcao e recolher a amplitude
            if direcao == -1 or direcao == 3:
                x -= 1
            if direcao == -2 or direcao == 2:
                y -= 1
            if direcao == -3 or direcao == 1:
                x += 1
            if direcao == 0:
                y += 1
            lista_posicoes.append((x, y))

        #colocar dentro da lista as maiores/menores posicoes e resetar os dados
        if letra == "H":
            maxX = max(lista_posicoes, key=lambda i: i[0])[0]
            maxY = max(lista_posicoes, key=lambda i: i[1])[1]
            minX = min(lista_posicoes, key=lambda i: i[0])[0]
            minY = min(lista_posicoes, key=lambda i: i[1])[1]
            lista_posicoes = [(0,0)]
            x,y=0,0
            lista_final.append((minX,minY, maxX,maxY))
    return lista_final

# calcular a direcao do robo
def calc_direcao(direcao, letra):
    if letra == "E":
        direcao -= 1
    if letra == "D":
        direcao += 1
    if letra == "H" or direcao == 4 or direcao == -4:
        direcao = 0
    return direcao




#self.assertEqual(robot("EEAADAAAAAADAAAADDDAAAHAAAH"),[(-9,-2,0,2),(0,0,0,3)]#
# self.assertEqual(robot("H"),[(0,0,0,0)])
