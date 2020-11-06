class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant: " + self.restaurant_name)
        print("Cuisine Type: " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open.")

res_kfc = Restaurant("KFC", "fast food")
res_kfc.describe_restaurant()
res_kfc.open_restaurant()
print("\n")

res_mc = Restaurant("McDonald's", "fast food")
res_mc.describe_restaurant()
res_mc.open_restaurant()
print("\n")

res_bk = Restaurant("Burger King", "fast food")
res_bk.describe_restaurant()
res_bk.open_restaurant()
print("\n")
