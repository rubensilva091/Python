import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

selector = [rock,paper, scissors]
k=1
while(k):
  player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  if (player == 1 or player ==2 or player ==3):
    break
print(selector[player])
print("\nComputer chose:")
computer = int(random.randrange(0,3))
print(selector[computer])

if (player==computer):
  print("Draw!")
elif ((player==0 and computer==1)or (player==1 and computer==2) or (player==2 and computer==0)):
  print("You Lose!")
else:
  print("You Win!")

