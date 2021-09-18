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
import random

user_input = int(
    input(
        "what do you choose? Type 0 for Rock, 1 for Paper or 2 fir Scissors."))
game = [rock, paper, scissors]
print(game[user_input])

computer_choice = random.randint(0, 2)
print(f"Computer chose {game[computer_choice]}")

if (user_input > computer_choice):
    if (user_input == 2 and computer_choice == 0):
        print("You lose")
    else:
        print("You win")

elif (user_input == computer_choice):
    print("Match Draw")
else:
    if (user_input == 1 and computer_choice == 2):
        print("you lose")
    else:
        print("you win")

