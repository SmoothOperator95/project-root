# topping.py
class Topping:
    TOPPINGS = {
        'Cherry': 0.00,
        'Whipped Cream': 0.00,
        'Caramel Sauce': 0.50,
        'Chocolate Sauce': 0.50,
        'Storios': 1.00,
        'Dig Dogs': 1.00,
        'T&T\'s': 1.00,
        'Cookie Dough': 1.00,
        'Pecans': 0.50
    }
    
    def __init__(self):
        self.toppings = []
    
    def add_topping(self, topping):
        if topping in self.TOPPINGS:
            self.toppings.append(topping)
    
    def get_total(self):
        return sum(self.TOPPINGS[topping] for topping in self.toppings)
    
    def __str__(self):
        return f"Toppings: {', '.join(self.toppings)}"