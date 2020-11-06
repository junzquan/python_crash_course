guests = ['Tom', 'Tim', 'Martin']
filename = 'guest_book.txt'
for guest in guests:
    name = input(f"{guest}, Are you comming to dinner? (Input your name if you come): ")
    if name == guest:
        with open(filename, 'a') as file:
            file.write(f"{guest}\n")
