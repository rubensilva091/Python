from data import *

# resources[i] -> é o valor inteiro, i -> é a key


def check(request):
    for i in MENU[request]["ingredients"]:
        if(resources[i] < MENU[request]["ingredients"][i]):
            print("Sorry there is not enough "+str(i))
            return -1
    return 1


def process(request, money):
    if (request == "report"):
        report(money)
        return 0
    if(check(request) == 1 and askmoney(request) == 1):
        for i in MENU[request]["ingredients"]:
            resources[i] -= MENU[request]["ingredients"][i]
        finalmensage(request)
        return MENU[request]["cost"]
    return 0


def report(money):
    for i in resources:
        if (i != "coffee"):
            print(i+" : " + str(resources[i])+"ml")
        else:
            print(i+" : " + str(resources[i])+"g")
    print("Money: €"+str(money)+"\n")


def askmoney(request):
    centimos20 = int(input("How many coins of 0.20€: "))
    centimos50 = int(input("How many coins of 0.50€: "))
    euro1 = int(input("How many coins of 1€: "))
    euro2 = int(input("How many coins of 2€: "))
    final = (centimos20*0.20) + (centimos50*0.50)+(euro1*1)+(euro2*2)
    if (final < MENU[request]["cost"]):
        if(final == 0):
            print("Sorry, you need to insert some coins.")
        else:
            print("Sorry that's not enough money. Money refunded.")
        return 0
    elif (final > MENU[request]["cost"]):
        print("Here is €" + str(final -
              MENU[request]["cost"])+" euros in change")
        return 1
    return 1


def finalmensage(request):
    print("Here is your "+request+".Enjoy! \n")


def coffemachine():
    money = 0
    while(True):
        request = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if (request == "off"):
            break
        while(request != "cappuccino" and request != "espresso" and request != "latter" and request != "off"):
            request = input(
                "That doesnt exist, please type the following options? (espresso/latte/cappuccino): ").lower()
        money += process(request, money)


coffemachine()
