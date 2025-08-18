def check_symptoms():
    print("Welcome to the Mental Health Checker")
    print("Please answer with 'yes' or 'no' ")

    symptoms={
        "Do you often have trouble sleeping or sleep too much?":0,
        "Do you feel tired or low energy even after rest? ":0,
        "Do you feel sad, anxious, or emoty most days?":0,
        "Do you find it hard to focus or make decisions?":0,
        "Do you feel hopeless,worthless,or guilty?":0
    }

    score=0
    for question in symptoms:
        answer=input(question+" ").strip().lower()
        if answer=="yes":
            score+=1

    print("\n Result: ")
    if score<=1:
        print("You're doing okay Just remember to rest and take breaks")
        print("Tip:Go for a walk, drink water, or call a friend")
    elif score<=3:
        print("You may need support Please talk to someone you trust")
    else:
        print("Tip:A counselor or therapist can really help")

    print("\n Remember:It's normal to feel low sometimes")
    print("Everybody is mad about something.You are not alone")

check_symptoms()                