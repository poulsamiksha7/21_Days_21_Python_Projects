import random

secret_number=random.randint(1,100)
attempts=0
print("🎲 Welcome to the Samiksha's Number Guessing Game")
print("Guess a Number between 1 to 100")

while True:
    guess = int(input("Enter your Guess: "))
    attempts += 1
    if guess==secret_number:
        print("Congratulations!! You Guessed it Correct in {attempts} attempts. You won the game")
        break
    elif guess>secret_number:
        print("Too High! Better Luck Next Time")
    else:
        print("Too Low! Better luck Next Time")