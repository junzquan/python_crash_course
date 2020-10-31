cities = {
    'Guangzhou': {
        'country': 'China',
        'population': 23000000,
        'fact': 'The biggest city in Guangdong province, China.',
    },

    'Beijing': {
        'country': 'China',
        'population': 21500000,
        'fact': "The capital of China."
    },

    'London': {
        'country': 'UK',
        'population': 8900000,
        'fact': "The capital of UK."
    },
}

for city, info in cities.items():
    print(city + ": ")
    for k, v in info.items():
        print(k + ": " + str(v))
    print("\n")