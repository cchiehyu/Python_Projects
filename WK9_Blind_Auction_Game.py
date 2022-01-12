from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to secret auction program!")

name = input("What is your name? \n ")
bid = int(input("What is your bid? \n"))

winner_record ={}
def find_highest_bidder(winner_record):
  highest_bid =0
  for people in winner_record:
    winner_value = winner_record[people]
    if winner_value > highest_bid:
      highest_bid = winner_value
      winner = people
  print(f"The winner is {winner}, with the bid of {highest_bid}.")
  
dict_game = {}
dict_game[name] = bid
print(dict_game)

conti_game = True
while conti_game:
  additional_player = (input("Is there any other users who want to bid? Type 'Yes' or 'No'.")).lower()
  if additional_player =="yes":
    clear()
    name = input("What is your name? \n ")
    bid = int(input("What is your bid? \n"))
    dict_game[name] = bid
    #print(dict_game)
  else:
    conti_game = False
    find_highest_bidder(dict_game)
    #max_bid =max(dict_game.values())
    #max_name = max(dict_game,key=dict_game.get)
    #print(f"The winner is {max_name}, with the bid of $ {max_bid}.")
