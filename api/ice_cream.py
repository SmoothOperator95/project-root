class IceCream:
    FLAVORS = {
        'Mint Chocolate Chip': 4.00,
        'Chocolate': 3.00,
        'Vanilla Bean': 3.00,
        'Banana': 3.50,
        'Butter Pecan': 3.50,
        'S\'more': 4.00
    }
    
    def __init__(self):
        self.flavors = []
    
    def get_flavors(self):
        return list(self.FLAVORS.keys())
    
    def add_flavor(self, flavor):
        if flavor in self.FLAVORS:
            self.flavors.append(flavor)
    
    def get_base(self):
        return self.flavors[0] if self.flavors else None
    
    def get_size(self):
        return len(self.flavors)
    
    def get_total(self):
        return sum(self.FLAVORS[flavor] for flavor in self.flavors)
    
    def get_num_flavors(self):
        return len(self.flavors)
    
    def __str__(self):
        return f"Ice Cream Flavors: {', '.join(self.flavors)}"
