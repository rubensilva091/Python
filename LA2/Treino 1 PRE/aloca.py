"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""
prefs1 = {10885:[1,5],40000:[5],10000:[1,2], 10004:[1,3], 10000:[1,2]}
prefs2 = {30000:[1],20000:[2],10000:[3]}

def aloca(prefs):
    alunos_alocados = [] #desnecessario, mas fundamental para nao me bugar o cerebro
    alunos_nao_alocados = []
    trabalhos_alocados=[]
    prefs_list=sorted(prefs.items())
    for (x,y) in prefs_list:
        for n in y:
            key=1
            if (not (n in trabalhos_alocados)):
                key=0
                trabalhos_alocados.append(n)
                alunos_alocados.append(x)
                break
        if (key==1):
            alunos_nao_alocados.append(x)
    return alunos_nao_alocados

aloca(prefs1)

# def test_aloca_1(self):
#   with test_timeout(self,1):
#       prefs1 = {10885:[1,5],40000:[5],10000:[1,2]}
#       self.assertEqual(aloca(prefs),[40000])
#
# def test_aloca_2(self):
#        with test_timeout(self,1):
#            prefs2 = {30000:[1],20000:[2],10000:[3]}
#            self.assertEqual(aloca(prefs),[])
