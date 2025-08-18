import random

horoscopes={
    "aries":["Today is a great day to take initiative!","Avoid unnecessary arguments","Focus on your goals"],
    "taurus":["Treat yourself with something nice!","Don't let laziness win today","Stability is your strength"],
    "gemini":["Talk your heart out today!","Your energy is contagious","Be careful with distractions"],
    "cancer":["Spend time with your loved ones","Your emotiones are your power","Do something creative"],
    "leo":["Take the lead today!","Your charm is magnetic","Share your ideas boldlt"],
    "virgo":["Organize your surroundings","Details matter-notice them","Your dedication is inspiring"],
    "libra":["Balance your work and rest","Beauty will find you today","Be fair , even to yourself"],
    "scorpio":["Something intense is coming!","Channel your passion wisely","Trust your instincts"],
    "sagittarius":["Go explore something new!","Adventure awaits you","Stay optimistic"],
    "capricon":["Discipline will reward you","Stick to your path","Take a break-you deserve it"],
    "aquarius":["Think differently today","You're a trendsetter","Don't be afraid to dream"],
    "pisces":["Let your imagination flow","Connect with your intuition","Express your feelings"]
}

print("Welcome to Daily Horoscope Generator! ")
sign=input("Enter your zodiac sign: ").lower()

if sign in horoscopes:
    print("Your message for today :")
    print(random.choice(horoscopes[sign]))
else:
    print("Oops! Invalid zodiac sign")