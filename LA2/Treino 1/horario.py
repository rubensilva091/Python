"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.

"""

ucs1 = {"la2": ("quarta", 16, 2), "pi": ("terca", 15, 1),
        "cp": ("terca", 14, 2), "so": ("quinta", 9, 3)}
alunos1 = {5000: {"la2", "cp"}, 2000: {"la2", "cp", "pi"},
           3000: {"cp", "poo"}, 1000: {"la2", "cp", "so"}}

ucs2 = {"la2": ("quarta", 16, 2), "pi": ("terca", 15, 1)}
alunos2 = {5000: {"la2", "pi"}, 2000: {"pi", "la2"}}

ucs3 = {"la2": ("quarta", 16, 2)}
alunos3 = {5000: {"la2"}}

# Isto esta javardo pra caralho, mas funciona, nao me julguem :'(
def horario(ucs, alunos):

    # encontrar UCS que se misturam
    sobreposicao_ucs = []
    for k1, tup1 in ucs.items():
        for k2, tup2 in ucs.items():
            if (k1 != k2):
                flag = 0
                hora_final1 = tup1[1]+tup1[2]
                hora_final2 = tup2[1]+tup2[2]
                if((hora_final1 >= tup2[1] and hora_final1 <= hora_final2)):
                    flag = 1
                if(hora_final1 >= tup2[1] and hora_final1 <= tup2[1] and tup1[1] >= tup2[1] and tup1[1] <= hora_final2):
                    flag = 1
                if(flag and tup1[0] == tup2[0]):
                    sobreposicao_ucs.append((k1, k2))

    # encontrar as ucs que os alunos teem que nao podem se misturar
    alunos_com_todas_ucs = []
    for (k, v) in alunos.items():
        all_possibles_ucs = []
        flag1 = 1
        flag2 = 1
        for uc1 in v:
            for uc2 in v:
                all_possibles_ucs.append((uc1, uc2))
        for uc in all_possibles_ucs:

            # detetar se o aluno possui alguma combinaçao que nao pode ter
            if (uc in sobreposicao_ucs):
                flag1 = 0

        # se o aluno poder frenquentar tudo, meter lo numa lista e contar as horas das aulas
        if (flag1):
            hours = 0
            for uc1 in v:

                # calcular horas de cada aluno
                for (kaux, vaux) in ucs.items():
                    if (uc1 == kaux):
                        hours += vaux[2]

                #A CADEIRA EXISTIR NAS UCS. por exemplo poo nao existe nas UCS, logo nao pode ser considerado
                if (uc1 not in ucs.keys()):
                    flag2 = 0

            if (flag2):
                alunos_com_todas_ucs.append((k, hours))

    # retornar o tuplo
    return sorted(alunos_com_todas_ucs, key=lambda i: (-i[1], i[0]))

#self.assertEqual(horario(ucs,alunos),[(1000, 7), (5000, 4)])
#self.assertEqual(horario(ucs,alunos),[(2000, 3), (5000, 3)])
