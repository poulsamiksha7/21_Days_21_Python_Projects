import random

print("Welcome to Flashcard Generator")
print("Create your own flashcards and test yourself!\n")

flashcards=[]
n=int(input("How many flashcards do you want to create? "))

for i in range(n):
    q=input(f"\n Enter question {i+1}: ")
    a=input(F"Enter answer {i+1}: ")
    flashcards.append((q,a))

print("|n Time to quiz yourself! Let's shuffle and begin...\n")
random.shuffle(flashcards)

score=0

for i,(q,a) in enumerate (flashcards):
    user_ans=input(f"Q{i+1}:{q}\nYour Answer: ").strip().lower()
    if user_ans==a.lower():
        print("Correct\n")
        score+=1
    else:
        print(f"Oops! Correct answer was: {a}\n ")

print(f"You got {score} out of {n} right!")

print("\n Learning is a treasure that will follow its owner everywhere...")
