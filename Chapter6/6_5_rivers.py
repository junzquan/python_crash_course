river_dict = {
    'nile': 'egypt',
    'yellow river': 'china',
    'amazon': 'brazil'
}

for river, country in river_dict.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in river_dict.keys():
    print(river.title())

for country in river_dict.values():
    print(country.title())
