dream_vacation = {}
next_person = 'yes'

while str(next_person) == 'yes':
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    next_person = input("Would you like to let another per repond? (yes / no) ")
    dream_vacation[name] = place

print("--- Poll Results ---")
for name, place in dream_vacation.items():
    print(name + " would like to go to " + place + ".")
    