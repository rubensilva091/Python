import re

#Função para Filtrar Toda a informação e colocar-la num dicionário
def filtrar_info(fd):
    data_processos = []

    # Seperar por Linhas
    lista_newlines = fd.split("\n")

    # Seperar cada Linha em uma array com as informações
    for line in lista_newlines:
        if len(line):
            processos = line.split("::")

        # Dicionario default para colocar as informações
            dict_processo = {
                "Pasta": "",
                "Data": "",
                "Nome": "????",
                "Pai": "????",
                "Mae": "????",
                "Observacao": ""
            }


            # Filtrar o Processo:
            for parametro in processos:
                # Recolher a data
                if (re.match("[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}", parametro)):
                    dict_processo["Data"] = parametro
                    continue
                # Recolher nr da Pasta
                if (re.match("[0-9]{1,4}", parametro)):
                    dict_processo["Pasta"] = parametro
                    continue
                # Recolher Informações que possuem Nomes Proprios (Começam por Letra maiscula)
                if (re.match("([A-Z]{1}[a-z]* ?)", parametro)):

                    if (re.search("[^A-Z]{1}\.", parametro)):
                        dict_processo["Observacao"] = parametro
                        continue
                    # Alocção ordenada de parametros ordenados:
                    if (dict_processo["Nome"] == "????"):
                        dict_processo["Nome"] = parametro
                        continue
                    if (dict_processo["Pai"] == "????"):
                        dict_processo["Pai"] = parametro
                        continue
                    if (dict_processo["Mae"] == "????"):
                        dict_processo["Mae"] = parametro
                        continue
                # Informação Inexistente
                if (re.match("", parametro)):
                    for (p1, p2) in dict_processo.items():
                        if dict_processo[p1] == "" or dict_processo[p1] == "????":
                            dict_processo[p1] = "!!NO INFO!!"
                            break

            data_processos.append(dict_processo)
    return data_processos


def calcular_freq_processos(data):
    dict_anos = {}
    total=0
    #Obter todos os processos por ano
    for processo in data:
        year = re.match("[0-9]{4}", processo["Data"]).group()
        if year not in dict_anos:
            dict_anos[year]=0
        total+=1
        dict_anos[year]+=1
    
    #Tabelar
    for (nome,counter) in sorted(dict_anos.items()):
        n = counter / total
        print("O ano tem "+str(nome) + " tem freq. de processos de:" + str(n))
    
    pass


# Falta descobrir o que está no "obs"
def calcular_freq_nomes_sec(data):
    #Variaveis Iniciais
    seculos = {}
    lista = ["Nome", "Pai", "Mae"]
    total_nomes_sec = {}
    total_apelidos_sec = {}

    #Ciclar toda a data e recolher toda a informação necessário para o exercício
    for processo in data:
        # Recolher o Ano e Fazer o Dicionario com o Seculo
        year = re.match("[0-9]{4}", processo["Data"]).group()
        year = int((int(year)-1) / 100)+1
        if (year not in seculos):
            seculos[year] = {"Primeiro_Nome": {}, "Apelido_Nome": {}}
            total_apelidos_sec[year] = 0
            total_nomes_sec[year] = 0

        # Recolher o Primeiro e o Ultimo Nome
        primeiro_nomes_lista = []
        apelidos_lista = []

        # Recolher Primerio e Ultimo Nome de Pai........
        for l in lista:
            if (processo[l] != "!!NO INFO!!"):
                primeiro_nome = re.search("^[A-Za-z]+", processo[l]).group()
                primeiro_nomes_lista.append(primeiro_nome)
                # Este if serve para os casos por exemplo "Ana Lopes Coelho (ou Ana Fernandes Lopes)"
                if (re.search("\)", processo[l])):
                    # Voltar a mandar o primeiro nome pra lista porque o Apelido é a unica coisa que difere
                    primeiro_nomes_lista.append(primeiro_nome)

                    # O apelido que está dentro de parentises
                    apelido_nome = re.search(
                        "[A-Za-z]*\)", processo[l]).group()[:-1]
                    apelidos_lista.append(apelido_nome)
                    # O apelido que está fora de parentises
                    apelido_nome = re.search(
                        "[A-Za-z]* \(", processo[l]).group()[:-2]
                    apelidos_lista.append(apelido_nome)
                else:
                    aux=processo[l]
                    #Em casos como: Maria Vale, Solteira
                    if (re.search(",", processo[l])):
                        aux=processo[l].split(",")[0]
                    apelido_nome = re.search("[A-Za-z]+$", aux).group()
                    apelidos_lista.append(apelido_nome)

        # Recolher Primerio e Ultimo Nome das observaçoes.
        if (processo["Observacao"] != "!!NO INFO!!"):
            obs_lista = re.findall(
                "(([A-Z]{1}[a-z]{1,} ?)+\,)", processo["Observacao"])
            #(nome,junk) pois a função findall está a criar um tuplo e nós queremos o primeiro membro
            for (nome, junk) in obs_lista:
                primeiro_nome = re.search("^[A-Za-z]+", nome[:-1]).group()
                primeiro_nomes_lista.append(primeiro_nome)
                apelido_nome = re.search("[A-Za-z]+$", nome[:-1]).group()
                apelidos_lista.append(apelido_nome)

        # Somar os Apelidos e Nomes de cada Seculo
        for n in primeiro_nomes_lista:
            if n not in seculos[year]["Primeiro_Nome"]:
                seculos[year]["Primeiro_Nome"][n] = 0
            total_nomes_sec[year] += 1
            seculos[year]["Primeiro_Nome"][n] += 1
        for n in apelidos_lista:
            if n not in seculos[year]["Apelido_Nome"]:
                seculos[year]["Apelido_Nome"][n] = 0
            total_apelidos_sec[year] += 1
            seculos[year]["Apelido_Nome"][n] += 1

    # Tabelar a Resposta:
    for (sec, data) in sorted(seculos.items()):
        print("Seculo: "+str(sec))
        print("\tNomes:")
        for (nome, counter) in data["Primeiro_Nome"].items():
            final = counter / total_nomes_sec[sec]
            print("\t\t"+str(nome)+" tem uma freq: "+str(final))
        print("\tApelidos:")
        for (nome, counter) in data["Apelido_Nome"].items():
            final = counter / total_nomes_sec[sec]
            print("\t\t"+str(nome)+" tem uma freq: "+str(final))
    return 0


def calcular_freq_relacao(data):
    #Criação de Variaveis
    total_relacoes =0
    dict_relacoes = {
        "Pai": 0,
        "Mae": 0
    }

    #Procurar as relações e somar las
    for processo in data:
        # Ver se o Pai ou Mae existe (podem ser desconhecido)
        if (processo["Pai"] != "!!NO INFO!!"):
            dict_relacoes["Pai"]+=1
            total_relacoes+=1

        if (processo["Mae"] != "!!NO INFO!!"):
            total_relacoes+=1
            dict_relacoes["Mae"]+=1

        #Relações que estão na observação
        relacoes = re.findall("[^A-Z]\,(([A-Z]{1}[a-z ]+)+)\.",processo["Observacao"])
        if(relacoes):
            relacoes = relacoes[0][0]

            #Tivemos de Adicionar estas 2 Excluisoes, pois eles sairam fora do nosso ER, Somente estes 2 casos!
            if not(re.match("Jeronimo Silva Coelho", relacoes) or re.match("Frei", relacoes)):
                if (relacoes not in dict_relacoes):
                    dict_relacoes[relacoes] =0 
                dict_relacoes[relacoes]+=1
                total_relacoes+=1

    #Criar a Tabela:
    print("Frequencias de Relacoes: ")
    for (rel,counter) in dict_relacoes.items():
        freq = counter/total_relacoes
        print("\tA relação "+str(rel)+" tem de freq: " +str(freq))


    return 0


#Criar o JSON
def criar_json(data,n):
    lista=[]
    counter=0
    for d in data:
        lista.append(d)
        if(counter > n-2):
            break
        counter+=1
    return lista

#Função para abrir o processos
with open('processos.txt') as file:
    #Abrir o file descriptor
    fd = file.read()
    #Colocar os processos na estrutura de dados
    processos_filtrados = filtrar_info(fd)

    #Criar um Menu e escolher a opção
    x = int(input("Digite qual exercicio:\n1-> Frequencia de Processos por Ano\n2-> Frequencia de Nomes Proprios e Apelidos por Seculo\n3-> Frequencia dos Tipos de Relação\nOpcao: "))
    if (x == 1):
        calcular_freq_processos(processos_filtrados)
    elif(x == 2):
        calcular_freq_nomes_sec(processos_filtrados)
    elif(x == 3):
        calcular_freq_relacao(processos_filtrados)

    #Criar o ficheiro JSON
    with open('processos.json', 'w') as file_output:
        dados_json= criar_json(processos_filtrados,20)
        file_output.write(str(dados_json))
    