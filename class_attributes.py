class Food:
    restaurant_name = "Food Point"
    tax = 0.05
    total_items = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Food.total_items += 1

    def show_food(self):
        print(f"Food   : {self.name}")
        print(f"Price  : Rs. {self.price}")
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Tax    : {Food.tax * 100}%")

    def add_price(self, amount):
        self.price += amount
        print(f"New price: Rs. {self.price}")

    def total_food(self):
        print(f"Total food items: {Food.total_items}")


food1 = Food("Pizza", 1500)
food2 = Food("Burger", 800)

print("--- Food 1 ---")
food1.show_food()
food1.add_price(200)
food1.total_food()

print()

print("--- Food 2 ---")
food2.show_food()
food2.total_food()

class Pizza:
    shop_name = "Pizza House"
    delivery_charges = 200
    total_pizzas = 0

    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price
        Pizza.total_pizzas += 1

    def show_pizza(self):
        print("Flavor:", self.flavor)
        print("Price:", self.price)
        print("Shop:", self.shop_name)
        print("Delivery:", self.delivery_charges)

pizza1 = Pizza("Chicken", 1200)
pizza2 = Pizza("Cheese", 1000)

pizza1.show_pizza()
pizza2.show_pizza()

print("Total pizzas:", Pizza.total_pizzas)