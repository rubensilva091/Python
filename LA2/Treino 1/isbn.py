'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

livros1 = {
    "Todos os nomes": "9789720047572",
    "Ensaio sobre a cegueira": "9789896604011",
    "Memorial do convento": "9789720046711",
    "Os cus de Judas": "9789722036757"
}

livros2 = {
    "Ola mundo": "0000000000001"
}


def isbn(livros):
    new_livros = []
    for (nome, codigo) in livros.items():
        counter=1
        lista_resultados=[]
        
        #Algoritmo de calculo do ISBN
        for n in codigo:
            if(counter<13):
                if (counter % 2 == 1):
                    lista_resultados.append(int(n)*1)
                else:
                    lista_resultados.append(int(n)*3)
            counter+=1
        soma_resultados=sum(lista_resultados)

        #se For um ISBN invalido, mete na lista
        if (soma_resultados%10 == 0):
            if(int(codigo[12]) != 0):
                new_livros.append(nome)
        else:
            if ((10 - (soma_resultados%10)) != int(codigo[12])):
                new_livros.append(nome)

    new_livros = sorted(new_livros)
    return new_livros


#self.assertEqual(isbn(livros), ["Memorial do convento", "Todos os nomes"])
#self.assertEqual(isbn(livros), ["Ola mundo"])
