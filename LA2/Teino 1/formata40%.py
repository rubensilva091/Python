"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""

codigo1 = "int x;x=0;x=x+1;"
codigo2 = "int main() {int x;x=0; x=x+1;}"


def formata(codigo):
    key = [";", "{", "}"]
    new_code = ""
    flag = 0
    counter = 0
    for k in codigo:
        # caso o codigo seja uma funcao
        if (k == "{"):
            flag = 1
        if k in key:
            new_code += k
            # colocar a string no meio
            new_code = new_code[:len(new_code)] + \
                '\n' + new_code[len(new_code):]
            if (flag):
                if(k != "}"):
                    new_code = new_code[:len(new_code)] + \
                        '  ' + new_code[len(new_code):]
                else:
                    # remove the last tab from a string
                    new_code = new_code[:-4]
                    new_code += k
        else:
            # caso exista muitas espacos na string original
            if (counter+1 <= len(codigo)-1):
                if (k == codigo[counter+1] and k == " " or flag and k == " "):
                    if(new_code[len(new_code)-1] ==" "):
                        new_code = new_code[:-1]

            new_code += k
        counter += 1
    if(flag == 0):
        new_code = new_code[:-1]
    return new_code


print(formata(codigo1))


#        with test_timeout(self,1):
#            codigo = "int x;x=0;x=x+1;"
#            self.assertEqual(formata(codigo),"int x;\nx=0;\nx=x+1;")
#
#        with test_timeout(self,1):
#            codigo = "int main() {int x;x=0;     x=x+1;}"
#            self.assertEqual(formata(codigo),"int main() {\n  int x;\n  x=0;\n  x=x+1;\n}")

# Caso o numero de espacos seja impar é necessario esta verificicaçao
# k == codigo[counter+1] and
# if(codigo[counter+1] == codigo[counter+2] and codigo[counter+2] != codigo[counter+3]):
#    print("entrou2")
#    new_code = new_code[:-1]
