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
prefs2 = {30000:[1,3,4,5],20000:[2,3,4],10000:[3,5]}
prefs3 = {10885:[1,5],40000:[5],10000:[1,2]}


def aloca(prefs):
    #Abrir as listas
    trabalhos_usados=[]
    alunos_sem_trabalho = []

    #percorrer cada aluno na lista ordenada
    for (numero, preferencias) in sorted(prefs.items()):
        flag=1

        #percorrer cada trabalho do aluno
        for trabalhos in preferencias:
            if trabalhos not in trabalhos_usados:
                trabalhos_usados.append(trabalhos)
                flag=0
                break

        #se o aluno nao tiver trabalho:
        if(flag):
            alunos_sem_trabalho.append(numero)
    return alunos_sem_trabalho


#self.assertEqual(aloca(prefs),[40000])
#elf.assertEqual(aloca(prefs),[])