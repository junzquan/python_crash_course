cat_filename = 'data/cats.txt'
dog_filename = 'data/dogs.txt'
try:
    with open(cat_filename, 'r') as cat_file:
        cats = cat_file.read()
        print(cats)

    with open(dog_filename, 'r') as dog_file:
        dogs = dog_file.read()
        print(dogs)
except FileNotFoundError:
    pass
