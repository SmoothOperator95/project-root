# ice_cream.py
class IceCream:
    FLAVORS = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }

    def __init__(self, flavor):
        if flavor not in self.FLAVORS:
            raise ValueError(f"Invalid flavor: {flavor}")
        self.flavor = flavor
        self.cost = self.FLAVORS[flavor]

    def get_flavor(self):
        return self.flavor

    def get_base(self):
        return self.flavor

    def get_total(self):
        return self.cost

    def __str__(self):
        return f"{self.flavor} Ice Cream - ${self.cost:.2f}"

