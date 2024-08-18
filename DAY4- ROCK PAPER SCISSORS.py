"""
DESCRIPTION : You are going to build a Rock, Paper, Scissors game.
You will need to use what you have learnt about randomisation and Lists to
achieve this.
"""

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

print("what do you wanna choose?")
input1=int(input("type 0 for ROCK\ntype 1 for PAPER\ntype 2 for SCISSORS"))
import random
input2=random.randint(0,2)
print("YOUR CHOICE :")
if input1==0:
    print("ROCK")
    print(rock)
elif input1==1:
    print("PAPER")
    print(paper)
elif input1==2:
    print("SCISSORS")
    print(scissors)
else:
    print("INVALID CHOICE")

print("COMPUTER'S CHOICE :")
if input2==0:
    print("ROCK")
    print(rock)
elif input2==1:
    print("PAPER")
    print(paper)
else :
    print("SCISSORS")
    print(scissors)

if input1==0 and input2==1:
    print("YOU LOOSE!!!")
elif input1==0 and input2==2:
    print("YOU WON!!!")
elif input1==1 and input2==0:
    print("YOU WIN!!!")
elif input1==1 and input2==2:
    print("YOU LOOSE!!!")
elif input1==2 and input2==0:
    print("YOU LOOSE!!!")
elif input1==2 and input2==1:
    print("YOU WIN!!!")
else:
    print("DRAW !!!")


