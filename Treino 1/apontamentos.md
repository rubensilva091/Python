sort dict by KEY:

dict1 = dict(sorted(x.items()))

sort dict by VALUE:

dict2 = dict(sorted(x.items(),  key=lambda i : i[1]))

Se eu quiser um tuplo dentro de um tuplo dentro de  um tuplo, simplesmente vou multiplicando pelas posicpes. Por exemplo
:key=lambda i : i[a][b][c].... por ai fora

sort dict by key descendente, simplesmente colocamos ", reverse = TRUE", por default vem ascendente

mas o reverse = True tem um problema!!!!! Da reverse EM TUDO, pra simplesmente usarmos o reverse num
caso muito espeficifico, usamos o "-" atras na variavel do lambda


Para dar sort dentro de sort....
{"EQUIPA" : (VITORIA, GOLO)}

equipas  ={ "benfica" : (5,7) , "porto" : (3,2), "sporting": (3,7) } 

sorted(equipas.items(),key= lambda e: (-e[1][0],e[1][1]))
O tuplo ira definir a prioridade dos membros a dar sort da esquerda pra direita. 




Colocar no meio de uma string, exemplo:

new_code = new_code[:len(new_code)] + '\n' + new_code[len(new_code):] #colocar a string no meio


array[1:] isto quer dizer que é da posiçao 1 do array até acabar incrementado
array[:1] isto quer dizer que é da posiçao 1 do array até acabar decrementando

.: o 1 nao conta!!!!
 

Remover letras no final string  str=str[:-2] 


funcao insert
list2 = ['a', 'b', 'c', 'd', 'e'] 
  
insert z at the front of the list
list2.insert(0, 'z')
['z', 'a', 'b', 'c', 'd', 'e']