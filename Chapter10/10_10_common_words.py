filename = 'data/count.txt'
try:
    with open(filename) as file:
        content = file.read()
        the_count = content.lower().count('the')
        print(f"The word 'the' in file is: {the_count}")
except FileNotFoundError:
    pass
