import random
from art import logo,vs
from game_data import data

def comparing_account_a():
  #Generate the random account a from the data
  option_a = random.choice(data)
  # print(option_a)
  option_a_name=option_a['name']
  option_a_follower=option_a['follower_count']
  option_a_description =option_a['description']
  option_a_country = option_a['country']

  #format the data into a printable format
  print(f"Compare A: {option_a_name}, a {option_a_description}, from {option_a_country}.")
  return [option_a_follower,option_a_name]

  # print(vs)
def comparing_account_b():
  #Generate the random account a from the data
  option_b = random.choice(data)
  # print(option_b)
  option_b_name=option_b['name']
  option_b_follower=option_b['follower_count']
  option_b_description =option_b['description']
  option_b_country = option_b['country']

  #format the data into a printable format
  print(f"Compare B: {option_b_name}, a {option_b_description}, from {option_b_country}.")
  return [option_b_follower,option_b_name]




def user_inputs(option_a_name,option_b_name):
  guess_follower = str(input(f"Guess who has more followers? Type 'A' for {option_a_name}, type 'B' for {option_b_name}:\n")).lower()
  return guess_follower




def compare_follower(option_a_follower,option_b_follower,guess_follower,option_a_name,option_b_name):
  if guess_follower=='a':
      if option_a_follower >= option_b_follower:
        print(f"You are right! The followers of {option_a_name} is greater than {option_b_name}! ")
        return True
      elif option_a_follower < option_b_follower:
        print(f"You are wrong :((the followers of {option_a_name} is less than {option_b_name}! ")
        return False
  else:
      if option_a_follower > option_b_follower:
        print(f"You are wrong:((the followers of {option_a_name} is greater than {option_b_name}!")
        return False
      else:
        print(f"You are right! The followers of {option_a_name} is less than {option_b_name}!")
        return True


# def reamin_winner():
#   compare_follower()

def higher_lower_game():
  counter = 0
  start_game = True
  print(logo)
  print("Welcome to the Higher-Lower Game!")
  while start_game == True:
    option_a_list = comparing_account_a()
    print(vs)
    option_b_list = comparing_account_b()
    guess_result = user_inputs(option_a_list[1],option_b_list[1])
    
    compare_result = compare_follower(option_a_list[0], option_b_list[0], guess_result, option_a_list[1], option_b_list[1])

    start_game = compare_result


    bigger_list=[]

    if start_game ==True:
      counter+=1
      print(f"Your score is {counter}")
    else:
      print(f"You're a loser, your score is {counter}.")
    

    
higher_lower_game()


