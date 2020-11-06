filename = 'programming_reasons.txt'
names = ['Tom', 'Tim', 'Martin']
with open(filename, 'a') as file:
    for name in names:
        reason = input(f"{name}, why do you want to learn programming? ")
        file.write(f"{reason}\n")
