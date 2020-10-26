pizzas = ['Meat Pizza', 'Fruit Pizza', 'BBQ Chicken Pizza']
friend_pizzas = pizzas[:]

pizzas.append('Pork Pizza')

friend_pizzas.append('Beff Pizza')

print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print('\n')

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
print('\n')