# This is a simple implementation of the game Rock, Paper, Scissors in Python.
print("Welcome to Rock, Paper, Scissors!")

#import random module to generate random numbers
import random

#ask player for input
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

#generate computer choice randomly
computer_choice=random.randint(0,2)

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

#print player choice
if player_choice == 0:
    print("You chose Rock.")
    print(rock)
elif player_choice == 1:
    print("You chose Paper.")
    print(paper)    
else:
    print("You chose Scissors.")
    print(scissors)

if player_choice == 0 and computer_choice == 1:
    print("Computer chose Paper. You lose!")
    print(paper)
elif player_choice == 0 and computer_choice == 2:
    print("Computer chose Scissors. You win!")
    print(scissors)
elif player_choice == 1 and computer_choice == 0:
    print("Computer chose Rock. You win!")
    print(rock)
elif player_choice == 1 and computer_choice == 2:
    print("Computer chose Scissors. You lose!")
    print(scissors)
elif player_choice == 2 and computer_choice == 0:
    print("Computer chose Rock. You lose!")
    print(rock)    
elif player_choice == 2 and computer_choice == 1:
    print("Computer chose Paper. You win!")
    print(paper)
else:
    print("It's a tie!")        
    