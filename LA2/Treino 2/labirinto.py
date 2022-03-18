'''
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.
'''
mapa1 = ["  ########",
         "# # #    #",
         "# # #### #",
         "# #      #",
         "# # # ####",
         "# # #    #",
         "#   # #  #",
         "##### ####",
         "#        #",
         "########  "]

mapa2 = ['   ',
         ' # ',
         '   ']


def caminho(mapa):
    return "NSEO"


# self.assertEqual(caminho(mapa1),"ESSSSSSEENNNEESSSSSEEESE")
# self.assertIn(caminho(mapa2),["EESS","SSEE"])
