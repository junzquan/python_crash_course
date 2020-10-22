guests = ['Tom', 'Mike', 'Peter']
message = ', I have found a bigger table.'
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
print('\n')

guests.insert(0, 'Tim')
guests.insert(2, 'Harry')
guests.append('Sherlock')

message = ', would you like to have dinner with me?'
print(guests[0] + message)
print(guests[1] + message)
print(guests[2] + message)
print(guests[3] + message)
print(guests[4] + message)
print(guests[5] + message)
print('\n')

message = ', I can only invite 2 people for dinner.'
print('Sorry, ' + guests[0] + message)
print('Sorry, ' + guests[1] + message)
print('Sorry, ' + guests[2] + message)
print('Sorry, ' + guests[3] + message)
print('Sorry, ' + guests[4] + message)
print('Sorry, ' + guests[5] + message)
print('\n')

message = ', I can not invite you to dinner.'
remove_guest = guests.pop()
print(remove_guest + message)
remove_guest = guests.pop()
print(remove_guest + message)
remove_guest = guests.pop()
print(remove_guest + message)
remove_guest = guests.pop()
print(remove_guest + message)
print('\n')

message = ', you are still invited.'
print(guests[0] + message)
print(guests[1], message)
print('\n')

del guests[0]
del guests[0]
print(guests)
