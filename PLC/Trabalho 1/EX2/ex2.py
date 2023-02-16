import re

string_iniciar_html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body></body></html>'


# Função Inicial para filtrar toda a informação para um dicionário
def filtrar_csv(fd):
    lista_newlines = fd.split("\n")
    data = []
    counter = 0
    # Seperar cada Linha em uma array com as informações
    for line in lista_newlines:
        # Dicionario para colocar a info do CSV
        dict_processo = {
            "id": "",
            "index": "",
            "data": "",
            "nome": "",
            "idade": "",
            "genero": "",
            "morada": "",
            "modalidade": "",
            "club": "",
            "email": "",
            "federado": "",
            "resultado": ""
        }
        if(line and counter > 0):
            # Colocar a Informação do dicionario apos uma pequena verificação
            row = line.split(",")
            if (re.match("[0-9a-z]{24}", row[0])):
                dict_processo["id"] = row[0]
            if (re.match("[0-9]{1,2}", row[1])):
                dict_processo["index"] = row[1]
            if (re.match("[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}", row[2])):
                dict_processo["data"] = row[2]
            if (re.match("[A-Za-z]+", row[3])):
                dict_processo["nome"] = row[3]
            if (re.match("[A-Za-z]+", row[4])):
                dict_processo["nome"] += " "+row[4]
            if (re.match("[0-9]{2}", row[5])):
                dict_processo["idade"] = row[5]
            if (re.match("[MF]{1}", row[6])):
                dict_processo["genero"] = row[6]
            if (re.match("[A-Za-z]+", row[7])):
                dict_processo["morada"] = row[7]
            if (re.match("[A-Za-z]+", row[8])):
                dict_processo["modalidade"] = row[8]
            if (re.match("[A-Za-z]+", row[9])):
                dict_processo["club"] = row[9]
            if (re.match("[a-zA-Z.]+@[a-zA-Z.]+", row[10])):
                dict_processo["email"] = row[10]
            if (re.match("true|false", row[11])):
                dict_processo["federado"] = row[11]
            if (re.match("true|false", row[12])):
                dict_processo["resultado"] = row[12]
        if (dict_processo["id"] != ""):
            data.append(dict_processo)
        counter += 1
    return data


# Função que devolve as datas mais extremas do nosso CSV
def datas_extremas(data):
    # Obter todas as datas numa lista e ordenar por ano -> mes -> dia
    aux_list = []
    for d in data:
        n = d["data"].split("-")
        aux_list.append(n)
        aux_list = sorted(aux_list, key=lambda i: (i[0], i[1], i[2]))

    # Passar os extremos para strings
    menor_data = aux_list.pop(0)
    menor_data_str = ""
    for i in menor_data:
        menor_data_str += i+"-"

    maior_data = aux_list.pop(-1)
    maior_data_str = ""
    for i in maior_data:
        maior_data_str += i+"-"

    return (menor_data_str[:-1], maior_data_str[:-1])


# Função que devolve um dicionário com cada modalidade por ano
def distribuicao_modalidade_ano(data):
    dict_distribuicao = {}
    for d in data:
        #obter o ano da data
        year = re.match("[0-9]{4}", d["data"]).group()
        #Obter a distribuição por modalidade
        if year not in dict_distribuicao:
            dict_distribuicao[year] = {}
        if d["modalidade"] not in dict_distribuicao[year]:
            dict_distribuicao[year][d["modalidade"]] = 0
        dict_distribuicao[year][d["modalidade"]] += 1

    return dict_distribuicao


# Função que devolve um dicionário com idades, generos e os escalões
def distribuicao_genero_idade(data):
    dict_distribuicao = {}
    for d in data:
        #obter a distribuição por genero e idade
        if d["idade"] not in dict_distribuicao:
            dict_distribuicao[d["idade"]] = {}
            dict_distribuicao[d["idade"]]["M"] = 0
            dict_distribuicao[d["idade"]]["F"] = 0
        dict_distribuicao[d["idade"]][d["genero"]] += 1
        # Obter os escaloes
        if (int(d["idade"]) < 35):
            dict_distribuicao[d["idade"]]["Escaloes"] = 1
        else:
            dict_distribuicao[d["idade"]]["Escaloes"] = 2
    return dict_distribuicao


# Função que devolve um dicionário com as moradas
def distribuicao_morada(data):
    dict_distribuicao = {}
    for d in data:
        #Obter a distribuição por modalidade
        if d["morada"] not in dict_distribuicao:
            dict_distribuicao[d["morada"]] = 0
        dict_distribuicao[d["morada"]] += 1
    return dict_distribuicao


# Função para calcular os atletas que estão aptos ou não
def aptos(data):
    dict_distribuicao = {}
    for d in data:
        #Obter o ano da Data
        year = re.match("[0-9]{4}", d["data"]).group()
        #Obter a distribuição por modalidade
        if year not in dict_distribuicao:
            dict_distribuicao[year] = {}
        if d["resultado"] not in dict_distribuicao[year]:
            dict_distribuicao[year][d["resultado"]] = 0
        dict_distribuicao[year][d["resultado"]] += 1

    # Calcular o Total para a percentagem:
    for year in dict_distribuicao:
        counter = 0
        for (key, value) in dict_distribuicao[year].items():
            counter += value
        if("true" in dict_distribuicao[year] and "false" in dict_distribuicao[year]):
            dict_distribuicao[year]["true"] = str(
                dict_distribuicao[year]["true"]/counter)+"  %"
            dict_distribuicao[year]["false"] = str(
                dict_distribuicao[year]["false"]/counter)+" %"
    return dict_distribuicao


# Função para escrever tabelas recebendo:
# data -> Dicionario com os parametros
# str1 -> string que escreverá o html
# nome_tabela -> String que dá o nome ao "h1" do html
# p_header -> String que dá o titulo à primeira coluna das tabelas
# anchor -> String com o path para o html
def draw_table_html(data, str1, nome_tabela, p_header, anchor):
    used_key = []
    str_header = '<body><h1><a href='+anchor+">"+nome_tabela + \
        '</a></h1><table><tr><th style="text-align: center">'+p_header+'</th>'
    str_table = ""
    for (year, var) in sorted(data.items()):
        str_table += '<tr><td style="text-align: center">'+str(year)+"</td>"
        for (key, value) in var.items():
            if key not in used_key:
                used_key.append(key)
                str_header += '<th style="text-align: center">' + \
                    str(key)+"</th>"
            str_table += '<td style="text-align: center">'+str(value)+"</td>"
        str_table += "</tr>"
    str_header += "</tr>"
    str_table += "</table>"
    str_final = re.sub("<body>", str_header+str_table, str1)

    return str_final

# Função "igual" à draw_table_html
# Esta teve de ser diferente pois é um dicionario bem mais simples
def draw_table_html_morada(data, str1, nome_tabela):
    str_header = '<body><h1><a href="morada.html">'+nome_tabela + \
        '</a></h1><table><tr><th style="text-align: center">Moradas</th><th style="text-align: center">Numero de Habitantes</th>'
    str_table = ''
    for (morada, value) in sorted(data.items()):
        str_table += '<tr><td style="text-align: center">'+str(morada)+'</td>'
        str_table += '<td style="text-align: center">'+str(value)+"</td></tr>"
    str_header += "</tr>"
    str_table += "</table>"
    str_final = re.sub("<body>", str_header+str_table, str1)
    return str_final


# Função para escrever os extremos no html
def data_extremas_html(datas, str1):
    str_header = '<body><h1><a href="extremos.html">Datas Extremas</a></h1><table><tr><th style="text-align: center">Datas</th>'
    str_table = '<tr><td style="text-align: center">'+str(datas[0])+'</td>'
    str_table += '<tr><td style="text-align: center">'+str(datas[1])+'</td>'
    str_header += "</tr>"
    str_table += "</table>"
    str_final = re.sub("<body>", str_header+str_table, str1)
    return str_final


# Função com os indicadores estatisticos
def indicadores(data, str1):
    datas_extremas_result = datas_extremas(data)
    distribuicao_modalidade_ano_result = distribuicao_modalidade_ano(data)
    distribuicao_genero_idade_result = distribuicao_genero_idade(data)
    distribuicao_morada_result = distribuicao_morada(data)
    aptos_result = aptos(data)

    # Desenhar as Tabelas no index.html
    str1 = draw_table_html_morada(
        distribuicao_morada_result, str1, "Distribuicao de Moradas")
    str1 = draw_table_html(
        aptos_result, str1, "Percentagem de Aptos", "Anos", "aptos.html")
    str1 = draw_table_html(distribuicao_genero_idade_result,
                           str1, "Distribuicao de Genero e Idades", "Idades", "idade_genero.html")
    str1 = draw_table_html(distribuicao_modalidade_ano_result,
                           str1, "Distribuicao de Modalidades por Ano", "Anos", "modalidade.html")
    str1 = data_extremas_html(datas_extremas_result, str1)
    return str1


# Função para escrever a lista da modalidade
# data -> Dicionario com os parametros
# str1 -> string que escreverá o html
def lista_final_modalidade(data, str1):
    str_header = "<body>"
    str_list = ""
    dist_mod = distribuicao_modalidade_ano(data)
    for (ano, vars) in sorted(dist_mod.items()):
        used_desp = []
        str_list += "<h1>"+ano+"</h1>"
        for (desp, counter) in vars.items():
            for d in data:
                y = re.match("[0-9]{4}", d["data"]).group()
                if d["modalidade"] == desp and y == ano:
                    if desp not in used_desp:
                        str_list += "<h2>"+desp+"</h2>"
                        used_desp.append(desp)
                    for (key, value) in d.items():
                        if(key != "id" and key != "index" and key != "resultado"):
                            str_list += "<p>"+key+" -> "+value+"</p>"
                    str_list += "<p>.</p>"
    str_final = str_header+str_list
    str_final = re.sub("<body>", str_final, str1)
    return str_final

# Função para escrever a lista do genero/idade
def lista_final_genero_idade(data, str1):
    used_idade = []
    str_header = "<body>"
    str_list = ""
    dist_genero = distribuicao_genero_idade(data)
    for (idade, vars) in sorted(dist_genero.items()):
        for d in data:
            if d["idade"] == idade:
                if idade not in used_idade:
                    str_list += "<h2>"+idade+" Anos </h2>"
                    used_idade.append(idade)
                for (key, value) in d.items():
                    if(key != "id" and key != "index" and key != "resultado"):
                        str_list += "<p>"+key+" -> "+value+"</p>"
                str_list += "<p>.</p>"
    str_final = str_header+str_list
    str_final = re.sub("<body>", str_final, str1)
    return str_final

# Função para escrever a lista das datas extremas
def lista_final_extremos(data, str1):
    str_header = "<body>"
    str_list = ""
    extremos = datas_extremas(data)
    for d in data:
        if (d["data"] == extremos[0] or d["data"] == extremos[1]):
            str_list += "<h1>"+ d["data"] + "</h1>"
            for (key, value) in d.items():
                if(key != "id" and key != "index" and key != "resultado"):
                    str_list += "<p>"+key+" -> "+value+"</p>"
            str_list += "<p>.</p>"
    str_final = str_header+str_list
    str_final = re.sub("<body>", str_final, str1)
    return str_final 

# Função para escrever a lista dos aptos
def lista_final_aptos(data, str1):
    str_header = "<body>"
    str_list = ""
    for d in data:
        for (key, value) in d.items():
            if(key != "id" and key != "index" and key != "resultado"):
                str_list += "<p>"+key+" -> "+value+"</p>"
        str_list += "<p>.</p>"
    str_final = str_header+str_list
    str_final = re.sub("<body>", str_final, str1)
    return str_final

# Função para escrever a lista das moradas
def lista_final_morada(data, str1):
    used_name = []
    str_header = "<body>"
    str_list = ""
    dist_moradas = distribuicao_morada(data)
    for (morada, counter) in sorted(dist_moradas.items()):
        for d in data:
            if d["morada"] == morada:
                if morada not in used_name:
                    str_list += "<h2>"+morada+"</h2>"
                    used_name.append(morada)
                for (key, value) in d.items():
                    if(key != "id" and key != "index" and key != "resultado"):
                        str_list += "<p>"+key+" -> "+value+"</p>"
                str_list += "<p>.</p>"
    str_final = str_header+str_list
    str_final = re.sub("<body>", str_final, str1)
    return str_final


# Filtrar o csv para um dicionário
processos_filtrados = []
with open("emd.csv") as file:
    fd = file.read()
    processos_filtrados = filtrar_csv(fd)

# Geramos Sempre todos os html do nada
# Esta parte do código é responsavel pela criação de todos os html e a sua informação
with open("index.html", "w") as file:
    string_index = indicadores(processos_filtrados, string_iniciar_html)
    file.write(string_index)

    # Abrir o html dos indicadores
    with open("extremos.html", "w") as file2:
        str_aux = lista_final_extremos(
            processos_filtrados, string_iniciar_html)
        file2.write(str_aux)
    with open("modalidade.html", "w") as file2:
        str_aux = lista_final_modalidade(
            processos_filtrados, string_iniciar_html)
        file2.write(str_aux)
    with open("idade_genero.html", "w") as file2:
        str_aux = lista_final_genero_idade(
            processos_filtrados, string_iniciar_html)
        file2.write(str_aux)
    with open("morada.html", "w") as file2:
        str_aux = lista_final_morada(processos_filtrados, string_iniciar_html)
        file2.write(str_aux)
    with open("aptos.html", "w") as file2:
        str_aux = lista_final_aptos(processos_filtrados, string_iniciar_html)
        file2.write(str_aux)
