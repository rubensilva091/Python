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
    equipas = {}
    for (equipa1, golo1, equipa2, golo2) in jogos:

        #inicializar as equipas
        if equipa1 not in equipas.keys():
            equipas[equipa1] = (0,0)
        if equipa2 not in equipas.keys():
            equipas[equipa2] = (0,0)

        #descobrir a equipa que ganhou
        equipa_vencedora = "empate"
        if (golo1<golo2):
            equipa_vencedora=equipa2
        elif (golo2<golo1):
            equipa_vencedora=equipa1

        #Criar a tabela final com os golos e as vitorias
        # {EQUIPA : (Vitoria, Diferenca de Golos)}
        for (team,(wins,dif_gols)) in equipas.items():
            if (equipa_vencedora == team):
                wins = wins+3
                equipas[equipa_vencedora] = (wins, dif_gols)
            if (equipa1 == team):
                if (equipa_vencedora == "empate"):
                    wins=wins+1
                equipas[equipa1] = (wins, dif_gols+(golo1-golo2))
            if (equipa2 == team):
                if (equipa_vencedora == "empate"):
                    wins=wins+1
                equipas[equipa2] = (wins, dif_gols+(golo2-golo1))

    #criar a lista final!
    lista_final = [(team, wins) for (team,(wins,dif_gols)) in sorted(equipas.items(), key=lambda  i: (-i[1][0],-i[1][1],i[0]))]

    return lista_final


#self.assertEqual(tabela(jogos),[('Porto', 4), ('Benfica', 4), ('Sporting', 2)])
#self.assertEqual(tabela(jogos),[('Benfica', 4), ('Porto', 4), ('Sporting', 2)])