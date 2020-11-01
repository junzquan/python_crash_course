sandwich_orders = ['beef sandwich', 'cheese sandwich', 'ham sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("These sandwiches are made: ")
print(finished_sandwiches)
