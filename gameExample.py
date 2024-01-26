secret_number = 75

def run_game():
    print("Welcome to the number game!")
    print("I have a secret number hidden - try to guess it!")
    print("When you think you know it, take a guess.  I will tell you if it is higher, lower, or correct.")
    myGuess(int(input("What number do you think it is?")))

def myGuess(guess):
    if guess < secret_number:
        print("Your guess is too low.")
        myGuess(int(input("What number do you think it is?")))
    elif guess > secret_number:
        print("Your guess is too high")
        myGuess(int(input("What number do you think it is?")))
    else:
        print("Congratulations - you figured it out!")

run_game()