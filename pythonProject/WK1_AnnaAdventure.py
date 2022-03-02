print('''
*******************************************************************************
                    |\|\
                   ..    \       .
                 o--     \\    / @)
                  v__///\\\\__/ @
                    {           }
                     {  } \\\{  }
                     <_|      <_|
               

                       -------------------------------
                             I AM ANNA I AM STINKY
                       -------------------------------
*******************************************************************************
''')
print("Welcome to Anna Monster Escape.")
print("Your mission is to beat Anna Tie-chuei Wang.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
crossroad= input("You\'re at Anna's house. Which room do you want to go? Type \"left\" or \"right\".\n").lower()
if crossroad == "left":
  lake = input('You\'ve come to the bathroom. There is a dog in the middle of the tub.\n Type "sleep" to take a nap.\n Type "go" to see the dog.\n').lower()
  if lake =="go":
    door = input("You have just meet Anna. She is so stinky.\n There is a box with 3 toys. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if door == "red":
      print("YEAH! You win! You just beat Anna!!!")
    elif door == "blue":
      print("Opps! She just Pee...Game Over...")
    else:
      print("You just step on her shit!!!! Game Over!!!!")
  else:
    print("You failed because you are too lazy...")
else:
  print("GAME OVER >\"<")
