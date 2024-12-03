# api/ice_storm.py

class IceStorm:
    FLAVORS = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }

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

    def __init__(self, base_flavor, size="medium"):
        if base_flavor not in IceStorm.FLAVORS:
            raise ValueError(f"Invalid base flavor: {base_flavor}")
        self.base_flavor = base_flavor
        self.size = size
        self.toppings = []
    
    def add_flavor(self, flavor):
        """Adds a new base flavor."""
        if flavor not in IceStorm.FLAVORS:
            raise ValueError(f"Invalid flavor: {flavor}")
        self.base_flavor = flavor

    def get_flavors(self):
        """Returns all available flavors."""
        return list(IceStorm.FLAVORS.keys())
    
    def get_base(self):
        """Returns the base flavor."""
        return self.base_flavor

    def get_size(self):
        """Returns the size of the ice cream."""
        return self.size
    
    def add_topping(self, topping):
        """Adds a topping to the ice cream."""
        if topping not in IceStorm.TOPPINGS:
            raise ValueError(f"Invalid topping: {topping}")
        self.toppings.append(topping)

    def get_total(self):
        """Calculates and returns the total cost."""
        total = IceStorm.FLAVORS[self.base_flavor]
        for topping in self.toppings:
            total += IceStorm.TOPPINGS[topping]
        return total
    
    def get_num_flavors(self):
        """Returns the number of base flavors (only 1 for now)."""
        return 1
    
    def __str__(self):
        """Returns a string representation of the Ice Storm."""
        flavor = self.base_flavor
        size = self.size
        toppings = ', '.join(self.toppings) if self.toppings else "No toppings"
        total = self.get_total()
        return f"Ice Storm - Flavor: {flavor}, Size: {size}, Toppings: {toppings}, Total: ${total:.2f}"
