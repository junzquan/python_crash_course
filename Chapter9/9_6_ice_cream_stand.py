class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant: " + self.restaurant_name)
        print("Cuisine Type: " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, served_number):
        self.number_served = served_number

    def increment_number_served(self, served_number):
        self.number_served += served_number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "ice cream")
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)


flavors = ['chocolate', 'watermelon', 'apple']
ics = IceCreamStand("icy house", flavors)
ics.show_flavors()
