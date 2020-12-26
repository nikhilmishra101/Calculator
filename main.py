from replit import clear
from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  isCalculating = True
  for symbol in operations:
    print(symbol) 
  while isCalculating == True:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")


    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if continue_calculating == "y":
      num1 = answer
    elif continue_calculating == "n":
      isCalculating = False
      clear()
      calculator()
    else:
      print( "Please enter the correct choice")

calculator()