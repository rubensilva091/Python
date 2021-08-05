import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

Welcome to the secret auction program
'''


listBids = {}

def newBider(name, bid):
    listBids[name] = bid

def bestBidder():
    bestbid = 0
    save = ""
    for bids in listBids:
        if (listBids[bids] > bestbid):
            bestbid = listBids[bids]
            save = bids
    print(f"The winner is {save} with a bid of ${bestbid}")

print(logo)

while (True):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    newBider(name, bid)
    cls()
    if (input("Are there any other bidders? Type 'yes'\n").lower() != "yes"):
        break

bestBidder()
