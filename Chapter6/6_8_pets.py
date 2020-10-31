jojo = {
    'name': 'jojo',
    'kind': 'dog',
    'owner': 'Tom',
}

bee = {
    'name': 'bee',
    'kind': 'cat',
    'owner': 'Tim',
}

pets = [jojo, bee]

for pet in pets:
    print(pet['owner'] + " owns a " + pet['kind'] + " names " + pet['name'] + ".")