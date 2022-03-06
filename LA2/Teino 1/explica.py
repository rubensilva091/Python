from typing import Counter


array = [("a", 5), ("c", 6), ("x", 3), ("o", 1), ("p", 9), ("a", 7)]

new_array = sorted(array, key=lambda i: i[1], reverse=False)

new_new_array = []


for x, y in new_array:
    if (x == "a"):
        new_new_array.append((x, y))

#print(new_new_array)

# [("a",5), ("a", 7)]


dict_ola = {1: "ola", 2: "salut", 3: "bonjour"}


#print(dict_ola)
#print((dict_ola.items()))
#print(list(dict_ola.items()))


#counter=0
#for x1 in dict_ola.items():
#    for x2 in dict_ola.items():
#        if (x1==x2):
#            print(x1)

Counter
for i in dict_ola.items():
    print(i)




