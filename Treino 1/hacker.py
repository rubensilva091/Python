"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""


log1 = [("****1234********", "maria@mail.pt"),
        ("0000************", "ze@gmail.com"),
        ("****1111****3333", "ze@gmail.com")]

log2 = [("0000************", "ze@gmail.com"),
        ("****1234********", "maria@mail.pt")]


def hacker(log):
    logs = {}

    for (cartao, mail) in log:
        #inicilizar os logs
        if (mail not in logs):
            logs[mail] = (cartao,len(cartao)-cartao.count("*"))
        else:
            cartao1 = cartao
            cartao2 = logs[mail][0]
            counter = 0 
            new_cartao = ""

            #concactenar os logs
            while(counter < len(cartao1)):
                flag = 1
                if(cartao1[counter] != "*" and flag):
                    flag = 0
                    new_cartao += cartao1[counter]
                if(cartao2[counter] != "*" and flag):
                    flag = 0
                    new_cartao += cartao2[counter]
                if(flag):
                    new_cartao += "*"
                counter += 1
            logs[mail] = (new_cartao,len(cartao)-new_cartao.count("*"))

    #criar a lista final ordenada com o mail e o codigo desoberto
    lista_final = [(name,code) for (code,(name, count)) in sorted(logs.items(), key=lambda i: (-i[1][1], i[0]))]
    return lista_final


# self.assertEqual(hacker(log),[("00001111****3333","ze@gmail.com"),("****1234********","maria@mail.pt")])
# self.assertEqual(hacker(log),[("****1234********","maria@mail.pt"),("0000************","ze@gmail.com")])
