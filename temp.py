# Write a method called addSubtract()
# This method should take a parameter called operation
# When the method is called, ask the user for two numbers
# Do the operation of the parameter to the inputs

num1 = [2, 5, 6, 98, 32, 123]
num2 = [5, 67, 89, 34, 1, 4]

def addSubtract(operation):
    num1 = int(input("What is the first number?"))
    num2 = int(input("What is the second number?"))
    if (operation == "add"):
        print(num1 + num2)
    else:
        print(num1 - num2)



addSubtract("add")
addSubtract("subtract")