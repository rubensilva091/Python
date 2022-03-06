"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""


codigo1 = "int x;x=0;x=x+1;"
codigo2 = "int main() {int x; x=0; x=x+1;}"
codigo3 = "int main() {int x;x=0; x=x+1;}"


#Copiei praticamente, este exercicio é jarvardo, vou admitir
def formata(codigo):
    final=""
    flag=1
    spaces=0
    i=0
    l=len(codigo)
    for c in codigo:
        i+=1
        if c==';':
            flag=1
            final=final+c+("\n" *(i<l)) + " "*spaces 
        elif(c=='{'):
            spaces+=2
            final=final+c+("\n" *(i<l)) + " "*spaces   
            flag=1
        elif(c=='}'):
            spaces-=2
            final=final[:-2] 
            final=final+c+("\n" *(i<l)) + " "*spaces 
            flag=1
        elif( (c==" "or c=="\n") and flag==1):
            continue
        else:
            final=final+c 
            flag=0
    print(final)
    return final


formata(codigo2)


#            self.assertEqual(formata(codigo),"int x;\nx=0;\nx=x+1;")
#            self.assertEqual(formata(codigo),"int main() {\n  int x;\n  x=0;\n  x=x+1;\n}")
