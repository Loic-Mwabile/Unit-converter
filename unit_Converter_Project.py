def length():
    while True:
        try:
            meter = float(input('Enter the value in meters: '))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Rest of the conversion logic...
    cm = 100 * meter
    inch = 39.37 * meter
    feet = 3.281 * meter
    yards = 1.093 * meter
    miles = 0.0006214 * meter

    print(f"{meter} meter is equal to {cm:.2f} cm, {inch:.2f} inch(es), {feet:.2f} feet, {yards:.2f} yard(s), and {miles:.2f} mile(s)" if meter == 1 else f"{meter} meters are equal to {cm:.2f} cm, {inch:.2f} inch(es), {feet:.2f} feet, {yards:.2f} yard(s), and {miles:.2f} mile(s)")
    choice()
def weight():
    while True:
        try:
            kilograms = float(input('Enter the value in kilograms: '))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Rest of the conversion logic...
    grams = 1000 * kilograms
    pounds = 2.20462 * kilograms
    ounces = 35.274 * kilograms
    tons = 0.00110231 * kilograms

    if kilograms == 1:
        print(f"{kilograms} kilogram is equal to {grams:.2f} grams, {pounds:.2f} pounds, {ounces:.2f} ounces, and {tons:.2f} tons.")
    else:
        print(f"{kilograms} kilograms are equal to {grams:.2f} grams, {pounds:.2f} pounds, {ounces:.2f} ounces, and {tons:.2f} tons.")
    choice()
def temperature():
    while True:
        try:
            celsius = float(input("Enter the value in Celsius: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Rest of the conversion logic...
    fahrenheit = (9/5) * celsius + 32
    kelvin = celsius + 273.15

    if celsius == 1:
        print(f"{celsius} degree Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
    else:
        print(f"{celsius} degrees Celsius are equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
    choice()
def time():
    while True:
        try:
            seconds = float(input('Enter a value in seconds: '))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Rest of the conversion logic...
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    years = days / 365.25

    if seconds == 1:
        print(f"{seconds} second is equal to {minutes:.2f} minutes, {hours:.2f} hours, {days:.2f} days, {weeks:.2f} weeks, and {years:.2f} years.")
    else:
        print(f"{seconds} seconds are equal to {minutes:.2f} minutes, {hours:.2f} hours, {days:.2f} days, {weeks:.2f} weeks, and {years:.2f} years.")
    choice()
def choice():
    option=input('Wanna do it again?(yes or no): ')
    option=option.casefold()
    while option!='yes' and option!='no':
        option=input('Type either yes or no: ')
        option=option.casefold()
    if option=='yes':
        start()
    elif option == "no":
        print("Thank you for using the unit converter!")
        exit()
def start():
    print("Choose a unit type:")
    for i, unit_type in enumerate(unit_types):
        print(f"{i+1}. {unit_type}")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): ")) - 1
            if choice >= 0 and choice < len(unit_types):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    unit_type = unit_types[choice]
    if unit_type == "length":
        length()
    elif unit_type == "weight":
        weight()
    elif unit_type == "temperature":
        temperature()
    elif unit_type == "time":
        time()

# Main program
print("Hello user! Hope that you are doing well.")
print("Here is a unit converter, it basically converts the basic units like meter, kilogram, second,... into other ones of the same type.")
print("What you need to do is to choose the type of unit you'd like to convert, enter a value and it does the job for you.")
print("Simple, isn't it? Let's try then.")
unit_types = ('length', 'weight', 'temperature', 'time')
start()