def get_moon_phase(day):
    if day<1 or day>30:
        return "Invalid day.Please enter a number between 1 and 30"
    
    if day==1 or day==30:
        return "🌚 New Moon"
    elif 2<= day<=7:
        return "🌒Waxing Crescent"
    elif day==8:
        return "🌓 First Quarter"
    elif 9<=day<=14:
        return "🌔 Waxing Gibbous"
    elif day==22:
        return "🌜 Last Quarter"
    elif 23 <=day<=29:
        return "🌒 Waxing Crescent"
    
print("Enter the day of the moon cycle(1-30): ")
try:
        day =int(input("Day:"))
        phase = get_moon_phase(day)
        print("Moon Phase:",phase)
except ValueError:
    print("Invalid Input. Please enter a Number")