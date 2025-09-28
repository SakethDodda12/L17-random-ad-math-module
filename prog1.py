import random

options = ["rock", "paper", "scissors"]
user = input("choose rock, paper or scissors: ")
computer = random.choice(options)

print("You chose: ", user)
print("Computer chose:", computer)

if user == computer:
    print("Its a tie")
elif user == "rock" and computer == "scissor":
    print("you won!")
elif user == "scissor" and computer == "paper":
    print("you won!")
elif user == "paper" and computer == "rock":
    print("you won!")
else:
    print("You lost.")