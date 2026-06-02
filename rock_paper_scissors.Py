import random

choices = ["rock", "paper", "scissors"]

print("===== ROCK PAPER SCISSORS =====")

while True:
    user = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
