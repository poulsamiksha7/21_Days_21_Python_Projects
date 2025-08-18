import os
from datetime import datetime

def write_letter():
    print("\n Let's write a letter to Future You!")
    today=datetime.now().strftime("%y-%m-%d")
    mood=input("How was your day?")
    message=input("What do you want to say to your future self? ")
    future_date=input("On which date should it open?(YYYY-MM-DD): ")

    filename=f"{future_date}.txt"
    with open(filename,"w")as f:
        f.write(f"Letter from {today}\n")
        f.write(f"Your mood: {mood}\n\n")
        f.write(f"Message: {message}\n")

        print(f"\n Saved! COme back on{future_date} to read it\n")

def read_letter():
    today=datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(f"{today}.txt"):
        with open(f"{today}.txt","r") as f:
            print("\n You've got a message from your past self:\n")
            print(f.read())
    else:
        print("\n No letter for today.Maybe write one?\n")

def main():
    print("Welcome to Future You Bot")
    while True:
        print("\n 1. Write a letter to future self")
        print("2.Check today's letter")     
        print("3. Exit")
        choice=input("Choose an option(1/2/3)")   

        if choice=="1":
            write_letter()
        elif choice=="2":
            read_letter()
        elif choice=="3":
            print("\n Bye! Keep dreaming!\n")
            break
        else:
            print("Invalid Input.Try again!")

main()            
        
