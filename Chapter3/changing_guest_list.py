guests = ['Tom', 'Mike', 'Peter']
message = ', would you like to have dinner with me?'
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)

out_guest = guests.pop(1)
print(out_guest + ' can not come.')

new_guest = 'Tim'
guests.append(new_guest)
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
