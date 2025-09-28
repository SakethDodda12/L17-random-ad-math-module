import random

playing = True
number = str(random.randint(0,9))

print("Guess a number from 0 to 9")
print("The games end when you guess correctly.")

while playing:
    guess = input("Guess!")
    
    if number == guess:
        print("You won the game")
        print("The number was: ", number)
        break
    else:
        print("The guess wasent quite right, try again!")