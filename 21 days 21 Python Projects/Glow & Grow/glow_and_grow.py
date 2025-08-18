import random

print("Welcome in Glow & Grow ! ")

quotes_gain=[
    "🤍You're not gaining weight, you've gaining strength!",
    "💪 Healthy weight is a form of self-love",
    "🍚 One bite at a time, one win at a time",
    "🌱 Nourish yourself to flourish"
]

quotes_loss=[
    "🔥 You're not losing weight, you've releasing what's not needed.",
    "⭐ Discipline today, confidence tomorrow!",
    "🍉 Light body, bright mind",
    "🌈 You're glowing from inside out!"
]

foods_gain=[
    "🍌 Banana shake with peanut butter",
    "🥛 Buffalo milk with jaggery at night",
    "🍍 Dry fruits soaked overnight",
    "🍅 Paneer bhurji with ghee paratha",
    "🍠 Sweet potato chaat"
]

foods_loss=[
    "🍚 Moong dal chilla with mint chutney",
    "🍵 Warm jeera water before meals",
    "🥗 Roti+ Sabji (less oil), no sugar",
    "🥙 Cucumber + sprouts salad",
    "🥗 Lauki soup with black pepper"
]

goal = input("Do you want to gain or lose weight?(gain/lose): ").lower()

print("\n ⭐ Your Quote of the Day ⭐")

if goal=="gain":
    print(random.choice(quotes_gain))
    print("\n 🥗 What to Eat Today(Weight Gain): ")
    print(random.choice(foods_gain))
elif goal=="loss":
    print(random.choice(foods_loss))
    print("\n 🥙 What to Eat Today (Weight Loss): ")
    print(random.choice(foods_loss))
else:
    print("🧘‍♀️ Just stay hydrated,rest well and take care of yourself 🧡")