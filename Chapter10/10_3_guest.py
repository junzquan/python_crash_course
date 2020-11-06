guests = ['Tom', 'Tim', 'Martin']
filename = 'guest_book.txt'
for guest in guests:
    come = input(f"{guest}, Are you comming to dinner? (Y/N): ")
    if come:
        with open(filename, 'a') as file:
            file.write(f"{guest}\n")
