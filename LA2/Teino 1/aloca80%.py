"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

#prefs1 = {1:2,3:4,4:3,2:1,0:0}

prefs1 = {10885:[1,5],40000:[5],10000:[1,2],10000:[1,2],10000:[1,2]}
#           self.assertEqual(aloca(prefs),[40000])


prefs2 = {30000:[1,3,4,5],20000:[2,3,4],10000:[3,5]}
#            self.assertEqual(aloca(prefs),[])

def aloca(prefs):
    projetos = []
    alunos_sem_projeto = []
    for (k,v) in sorted((prefs.items())):
        for n in v:
            flag=1
            if (n not in projetos):
                projetos.append(n)
                flag=0
                break
        if (flag):
            alunos_sem_projeto.append(k)
    return sorted(alunos_sem_projeto)


print(aloca(prefs1))

blacklist=[10885]
