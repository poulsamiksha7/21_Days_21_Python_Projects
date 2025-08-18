print("💧 Welcome to Water Intake Calculator 💧")

weight=float(input("Enter your weight in kg: "))
gender=input("Enter your gender (male/female/other):").strip().lower()

water_ml=weight*35
water_liters=water_ml/1000

if gender=="female":
    note="⭐Tip:Drink warm water with lemon in morning!"
elif gender=="male":
    note="😍Tip: Start your day with 1 glass from a copper bottle!"
else:
    note="🤍Stay hydrated, no matter your identity!"

print(f"\n💧 You should drink approx {water_liters:.2f}liters of water per day.")
print(note)
print("Ayurveda:Sip slowly,not gulp. Stay cool, stay hydrated")