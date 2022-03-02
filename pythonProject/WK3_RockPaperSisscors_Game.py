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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_input])

computer = random.randint(0,2)
print(f"Computer choose {computer}: ")
print(game_images[computer])


if user_input ==2:
  if computer ==2:
    print("Draw!")
  elif computer == 0:
    print("You Lose...")
  elif computer == 1:
    print("You Win!!")
if user_input == 0:
  if computer ==2:
    print("You win!!")
  elif computer == 0:
    print("Draw!")
  elif computer ==1:
    print("You lose...")
if user_input == 1:
  if computer == 2:
    print("You Lose...")
  elif computer == 0:
    print("You Win!!")
  elif computer == 1:
    print("Draw!")

