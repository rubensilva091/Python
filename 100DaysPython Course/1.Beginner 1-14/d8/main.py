logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

def enconde():
  string=""
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  for i in text:
    string  += chr(ord(i) + shift)  #increment letter
  return string

def decode():
  string=""
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  for i in text:
    string  += chr(ord(i) - shift) #decrement letter
  return string

while(True):
  string=""
  selector = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if selector == "encode":
    string=enconde()
  elif selector == "decode":
    string=decode()
  print(string)
  if (input("Type 'no' to quit.\n")=="no"):
    break

