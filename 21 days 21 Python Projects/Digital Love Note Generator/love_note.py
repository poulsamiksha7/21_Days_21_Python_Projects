import random
import webbrowser

names=input("Enter your Loved Ones Name: ")

message=[
    f"Hey {names},\n You light up my world like Diwali lights.\n Have a magical day,my sunshine",
    f"Dearest{names},\n Just a reminder that you're amazing.\n Keep smiling for me",
    f"{names},\nMy heart does a happy dance whenever I think of you"
]

songs=[
    "https://youtu.be/odVptmgIcD0?si=x16LmlprOaYAXLGM", #Tum Mile
    "https://youtu.be/Qdz5n1Xe5Qo?si=jH3Y0X2Y4K0Pfe09",#Tera ban jaunga
    "https://youtu.be/gvyUuxdRdR4?si=ssVqcCI5rjjbZQoB", #Raataan Lambiyan
    "https://youtu.be/Cb6wuzOurPc?si=SetmHOEGOJNnDvfj" #Tum se hi
]

msg=random.choice(message)
link=random.choice(songs)

print("\n"+msg)
print("\n Pla our song:"+link)

open_now=input("\n Wanna hear it now?(y/n): ").lower()
if open_now=="y":
    webbrowser.open(link)