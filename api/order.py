# order.py
from .ice_cream import IceCream
from .topping import Topping

class Order:
    def __init__(self):
        self.ice_creams = []
        self.toppings = []

    def add_flavor(self, flavor):
        ice_cream = IceCream(flavor)
        self.ice_creams.append(ice_cream)

    def add_topping(self, topping):
        topping_item = Topping(topping)
        self.toppings.append(topping_item)

    def get_flavors(self):
        return [ice_cream.get_flavor() for ice_cream in self.ice_creams]

    def get_base(self):
        return [ice_cream.get_base() for ice_cream in self.ice_creams]

    def get_size(self):
        return len(self.ice_creams)

    def get_num_flavors(self):
        return len(self.ice_creams)

    def get_total(self):
        total_cost = sum(ice_cream.get_total() for ice_cream in self.ice_creams)
        total_cost += sum(topping.get_total() for topping in self.toppings)
        return total_cost

    def __str__(self):
        ice_cream_details = "\n".join(str(ice_cream) for ice_cream in self.ice_creams)
        topping_details = "\n".join(str(topping) for topping in self.toppings)
        return f"Order:\n{ice_cream_details}\nToppings:\n{topping_details}\nTotal: ${self.get_total():.2f}"
