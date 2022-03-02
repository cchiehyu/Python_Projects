from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(account):
  # Format account data into printable format.
  account_name = account_a["name"]
  account_descr = account_a["description"]
  account_country = account_a['country']
  print(f"{account_name}, a {account_descr}, from {account_country}.")

# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
  if a_followers >b_followers:
    return guess =="a"
  else:
    return guess =="b"


#Display art
print(logo)
score = 0

game_should_continue = True
account_b = random.choice(data)

# Make game repeatable.
while game_should_continue:
  # Generate a random account from the game data.
  
  # Make B become the next A.
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear screen between rounds.
  clear()
  print(logo)
  
  # Feedback.
  if is_correct:
    # Score Keeping.
    score += 1
    print(f"Right, current score {score}")
  else:
    game_should_continue = False
    print(f"Wrong, current score {score}")
    print("Wrong")
