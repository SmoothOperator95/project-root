# topping.py
class Topping:
    TOPPINGS = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Storios": 1.00,
        "Dig Dogs": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50
    }

    def __init__(self, topping):
        if topping not in self.TOPPINGS:
            raise ValueError(f"Invalid topping: {topping}")
        self.topping = topping
        self.cost = self.TOPPINGS[topping]

    def get_total(self):
        return self.cost

    def __str__(self):
        return f"{self.topping} - ${self.cost:.2f}"
