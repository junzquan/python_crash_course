countries = ['China', 'Japan', 'German', 'United Kingdom', 'France']
print("There are " + str(len(countries)) + " countries in the list.")

print(sorted(countries))
print(sorted(countries, reverse=True))
print(countries)

countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

countries.reverse()
print(countries)