from art import logo
#calculator
print(logo)

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

#Create dictionary called operations value = functions
operations ={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1 = float(input("What is the first number:"))

  for symbols_print in operations:
    print(symbols_print)


  should_continue = True
  while should_continue == True:

    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What is the next number:"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol}{num2}={answer}")

    user_conti = input(f"Type 'y' to continue with {answer},type 'n' to start a new calculation.").lower()

    if user_conti =='y':
      num1 = answer
    
    if user_conti == 'n':
      print("Here is your new calculator.")
      calculator()

calculator()
