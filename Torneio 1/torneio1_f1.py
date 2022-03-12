"""

Implemente uma função que, dada uma lista com registos de instantes de tempo e nome de piloto, 
descrevendo os tempos de passagem pela meta dos varios pilotos numa corrida de F1, 
devolva a lista com os nomes dos pilotos com a volta mais rápida ordenada por ordem alfabética. 
Assuma que todos os pilotos iniciaram a prova no instante 0.

"""

log1 = [(20, "Alonso"), (20, "Rosberg"), (25, "Hamilton"), (35, "Rosberg"), (50, "Alonso"), (55,
                                                                                             "Hamilton"), (70, "Hamilton"), (80, "Rosberg"), (70, "Alonso"), (100, "Alonso"), (120, "Hamilton")]
log2 = [(20, "Alonso"), (25, "Hamilton"), (50, "Alonso"),
        (55, "Hamilton"), (70, "Hamilton"), (70, "Alonso")]

log3 = []

log4=[(20, "Alonso"),(0, "Hamilton"),(55, "Hamilton"),(0,"ala")]

#Isto foi feito no teste, está javardo pra caralho
def formula1(log):
    f1_pilots = {}
    dict_final = {}
    # Guardar todas as voltas por corredor
    for tempo, piloto in sorted(log, key=lambda i:i[0]):
        f1_pilots.setdefault(piloto, []).append(tempo)

    # calcular
    for pilot, list_time in f1_pilots.items():
        if pilot not in dict_final.keys():
            dict_final[pilot] = list_time[0]
        for i in range(len(list_time)-1):
            volta = list_time[i+1]-list_time[i]
            if (volta < dict_final[pilot] and volta ):
                dict_final[pilot] = volta
    
    aux_lista = sorted(dict_final.items(), key=lambda i: (i[1], i[0]))
    final_lista = []
    min_time=0
    if(aux_lista):
        min_time = aux_lista[0][1]
    for name, time in aux_lista:
        if min_time == time:
            final_lista.append(name)

    

    #ordernar
    #final_lista2=[name1 for name1,namelower in sorted(final_lista, key=lambda i: i[1])]
    return sorted(final_lista)

print(formula1(log4))


#self.assertEqual(formula1(log),['Hamilton', 'Rosberg'])
# self.assertEqual(formula1(log),['Hamilton'])

# for (time,pilot) in log:
#    if pilot not in f1_pilots:
#        f1_pilots[pilot]=[time]
#    else:
#        for p,t in f1_pilots.items():
#            if p == pilot:
#                t=f1_pilots[pilot]
#                t.append(time)
#                f1_pilots[pilot]=t
