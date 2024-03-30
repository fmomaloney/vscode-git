"""
git test Dave

"""
import math
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# control + b to hide vs code file tree
# alt + z to wrap text in editor


print()
playerchoice = input("Enter: \n1 for rock\n2 for paper\n3 for scissors\n\n")
player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("numbers 1-3 please")

compchoice = random.choice("123")
computer = int(compchoice)

print("you chose " + str(RPS(player)).replace('RPS.', ''))
print("python chose " + str(RPS(computer)).replace('RPS.', ''))

if player == 1 and computer == 3:
    print("you win! 😃")
elif player == 2 and computer == 1:
    print("you win! 😃")
elif player == 3 and computer == 2:
    print("you win! 😃")
elif player == computer:
    print("tie game")
else:
    print("python wins")
