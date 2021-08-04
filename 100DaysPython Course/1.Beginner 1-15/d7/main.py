import random
import os
import listas1


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def finder(lista, letter):
  for i in range(len(string)):
    if (string[i]== letter.lower()):
      lista.append(i)
  return lista

def jogo(lista, n, listaErros):
  espacosVazios = ""
  for i in range(n):
        if (i in lista):
          espacosVazios+= string[i] +" "
        else:
          espacosVazios += "_ "         
  print(espacosVazios)
  if(espacosVazios.find("_")==-1):
    return 1
  return 0
  
winner=0
loser=0
k=0
test=-1
lista = []
listaErros = []
string = random.choice(listas1.word_list)
loser=7
while(True):
  cls() #limpar a consola
  winner=jogo(lista, len(string), listaErros)
  if winner==1 or loser==0:
    break
  print(listas1.stages[k-1])
  letter=input("Guess a letter : ")
  while(len(letter)>1):
    letter=input("Guess a letter : ")
  test= string.find(letter.lower())  #string.find retorna a posição da string onde existe
  if (test>= 0):
    lista = finder (lista, letter)
  else:
    k-=1
    loser-=1



if (winner==1):
  print("\n\nU WON!")
if (loser==0):
  print("\n\nU LOST!")