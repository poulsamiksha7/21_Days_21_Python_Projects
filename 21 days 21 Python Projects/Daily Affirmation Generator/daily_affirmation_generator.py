import random
import time
from datetime import datetime

print("🤍Welcome to Your Daily Affirmation Ritual")
print("Take a deep breath.. Inhale...Exhale")

time.sleep(2)

affirmations=[
    "I am enough, just as i am.",
    "I am greatful,mindful, and calm",
    "I radiate confidence, beauty, and grace",
    "The universe supports my growth",
    "I am worthy of love and joy",
    "I trust the timing of my life",
    "My energy is sacred. I protect it",
    "I choose peace over perfection",
    "My dreams are valid and within reach",
    "I let go of what no longer serves me"
]

chosen=random.choice(affirmations)

print("\n Your affirmation for", datetime.now().strftime("%A,%d,%B %y"))
time.sleep(1.5)
print("\n 🙂"+ chosen)
time.sleep(1.5)

save=input("\n Do you want to save this to your Affirmation Diary? (yes/no):").lower()

if save=="yes":
 with open("affirmation_diary.txt","a") as file:
  file.write(f"{datetime.now().strftime("%Y-%m-%d")}-{chosen}\n")

  print("Saved to your diary.Come back tomorrow")
else:
 print("Stay blessed and see you tomorrow!")
