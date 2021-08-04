import random

size=int(input("Welcome to the PyPassword Generator!\nHow many letteres would you like in your password\n"))
symbols=int(input("How many symbols would you like?\n"))
numbers=int(input("How many numbers would you like?\n"))
letters=size-symbols-numbers
string_letters="qwertyuioplkjhgfdsamnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"
string_symbols="!#$%&/()=?»`^*:;>|\<,.-~´+@€£§"
string_number="0123456789"
password= ""

for i in range(size):
  selector=random.randrange(0,2)
  if (selector==0 and symbols>0):
    r=random.randrange(0,len(string_symbols))
    password = password + str(string_symbols[r])
    symbols -=1
  elif (selector==1 and numbers>0):
    r=random.randrange(0,len(string_number))
    password = password + str(string_number[r])
    numbers -=1
  else:
    r=random.randrange(0,len(string_letters))
    password = password + str(string_letters[r])
    
print(password)