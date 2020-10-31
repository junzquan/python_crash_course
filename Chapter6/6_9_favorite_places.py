favorite_places = {
    'Tom': ['Guangzhou', 'Beijing'],
    'Tim': ['Tokyo'],
    'Mike': ['New York', 'London', 'Paris'],
}

for name, places in favorite_places.items():
    if len(places) <= 1:
        print(name.title() + "'s favorite place is " + places[0])
    else:
        print(name.title() + "'s favorite places are")
        for place in places:
            print("\t" + place)
    print("\n")
