class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant: " + self.restaurant_name)
        print("Cuisine Type: " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant("KFC", "fast food")
restaurant.describe_restaurant()
restaurant.open_restaurant()
