import random
import time

print("🤍Welcome to the Crush Compatibility Checker🧡")
print("-",50)

your_name=input("Enter your name: ")
crush_name= input("Enter your crush's name: ")

print("\n Calculating Compatibility...")
time.sleep(2)

compatibility=random.randint(40,100)

if compatibility>=90:
    message="😍Perfect Match! Start Wedding Prepration😍"
elif compatibility>=75:
    message="🧡You're made for each other!"
elif compatibility>=60:
    message="🤍Cute Vibe! Could be something real!"
elif compatibility>=50:
    message="🙂Hmmmm... Maybe a Slow Burn?"
else:
    message="💔 Friendzone alert... Or just prank them?"

print(f"\n 🤍{your_name}+{crush_name}={compatibility}% Compatibility🧡")
print(message)