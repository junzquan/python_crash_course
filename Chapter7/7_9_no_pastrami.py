sandwich_orders = ['beef sandwich', 'cheese sandwich', 'ham sandwich', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The Deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("These sandwiches are made: ")
print(finished_sandwiches)
