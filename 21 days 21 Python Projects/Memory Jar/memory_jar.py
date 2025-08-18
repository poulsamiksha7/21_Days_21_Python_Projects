import os
import random
from datetime import datetime

FILENAME="memory_jar.txt"

if not os.path.exists(FILENAME):
    with open(FILENAME,"w"):pass

with open(FILENAME,"r") as f:
    memories=[line.strip()for line in f if line.strip()]

print("\n Welcome to your Upgraded Memory Jar\n") 

if memories:
    print("Flashback to 3 past memories: \n")
    for mem in random.sample(memories,min(3,len(memories))):
        print(f"-{mem}")
    print()

choice=input("Want to add today's mood? (yes/no/export): ").strip().lower()

if choice=="yes":
    mood= input("What's your mood?").strip().capitalize()

    memory=input("YOur memory today: ").strip()
    time_now=datetime.now().strftime("%Y-%m-%d %H:%M")

    if memory:
        formatted=f"[{time_now}] ({mood}) {memory}"
        with open(FILENAME,"a")as f:
            f.write(formatted+"\n")
        print("\n Saved to your jar with timestamp & mood !")
    else:
        print("No memory entered ")

elif choice=="export":
    export_name="memory_export.txt"
    with open(export_name,"w") as f:
        f.write("My full memory Jar\n\n")
        f.write("\n".join(memories))
    print(f"\nMemory jar exported to '{export_name}'")     

else:
    print("Okay,come back tomorrow with a full heart!")           

