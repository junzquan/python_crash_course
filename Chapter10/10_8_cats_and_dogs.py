cat_filename = 'cats.txt'
dog_filename = 'dogs.txt'
try:
    with open(cat_filename, 'r') as cat_file:
        cats = cat_file.read()
        print(cats)

    with open(dog_filename, 'r') as dog_file:
        dogs = dog_file.read()
        print(dogs)
except FileNotFoundError:
    print("Make sure you have cats.txt file and dogs.txt file.")
