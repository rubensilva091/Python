'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''


jogos1 = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
jogos2 = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2)]




def tabela(jogos):
    return []




#def test_tabela_1(self):
#    with test_timeout(self,1):
#        jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
#        self.assertEqual(tabela(jogos),[('Porto', 4), ('Benfica', 4), ('Sporting', 2)])

#def test_tabela_2(self):
#    with test_timeout(self,1):
#        jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",2,"Benfica",1),("Sporting",2,"Porto",2)]
#        self.assertEqual(tabela(jogos),[('Benfica', 4), ('Porto', 4), ('Sporting', 2)])