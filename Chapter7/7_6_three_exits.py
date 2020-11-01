#version 1
age = 0
while str(age) != 'quit':
    age = input("Input your age(input 'quit' to exit): ")
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age >= 3 and age < 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")

# version 2
active = True
while active:
    age = input("Input your age(input 'quit' to exit): ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age >= 3 and age < 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
    

# version 3
while True:
    age = input("Input your age(input 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free.")
    elif age >= 3 and age < 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")
        