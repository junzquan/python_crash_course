martin = {
    'first_name': 'Martin',
    'last_name': 'Zheng',
    'age': 24,
    'city': 'Guangzhou',
}

tom = {
    'first_name': 'Tom',
    'last_name': 'Zhang',
    'age': 27,
    'city': 'Beijing',
}

tim = {
    'first_name': 'Tim',
    'last_name': 'Cheng',
    'age': 30,
    'city': 'Shenzhen',
}

people = [martin, tom, tim]

for person in people:
    print(person['first_name'].title() + " " + person['last_name'] + 
        " who lives in " + person['city'] + " is " + str(person['age']) +
        " years old.")
