magicians = ['David Copperfield', 'Doug Henning', 'Siegfried and Roy']

def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] = "The Great " + magicians[i]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

make_great(magicians)
show_magicians(magicians)
