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

restaurant = Restaurant("KFC", "fast food")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("The restaurant has served " + str(restaurant.number_served) + " customers.")

restaurant.set_number_served(23)
print("The restaurant has served " + str(restaurant.number_served) + " customers.")

restaurant.increment_number_served(23)
print("The restaurant has served " + str(restaurant.number_served) + " customers.")
