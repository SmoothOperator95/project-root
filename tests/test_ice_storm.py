# tests/test_ice_storm.py

import unittest
from api.ice_storm import IceStorm

class TestIceStorm(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.ice_storm = IceStorm("Chocolate", "medium")
    
    def test_get_flavors(self):
        """Test if the available flavors are correct."""
        flavors = self.ice_storm.get_flavors()
        self.assertIn("Chocolate", flavors)
        self.assertIn("Mint Chocolate Chip", flavors)
    
    def test_add_flavor(self):
        """Test if a new base flavor can be added."""
        self.ice_storm.add_flavor("Vanilla Bean")
        self.assertEqual(self.ice_storm.get_base(), "Vanilla Bean")
    
    def test_add_topping(self):
        """Test if toppings are correctly added."""
        self.ice_storm.add_topping("Caramel Sauce")
        self.assertIn("Caramel Sauce", self.ice_storm.toppings)
    
    def test_get_total(self):
        """Test the cost calculation with toppings."""
        self.ice_storm.add_topping("Caramel Sauce")
        self.ice_storm.add_topping("Whipped Cream")
        total = self.ice_storm.get_total()
        self.assertEqual(total, 3.50)  # Chocolate + Caramel Sauce + Whipped Cream
    
    def test_invalid_flavor(self):
        """Test if invalid flavors raise errors."""
        with self.assertRaises(ValueError):
            self.ice_storm.add_flavor("Strawberry")
    
    def test_invalid_topping(self):
        """Test if invalid toppings raise errors."""
        with self.assertRaises(ValueError):
            self.ice_storm.add_topping("Sprinkles")
    
    def test_str_method(self):
        """Test if the string representation is correct."""
        self.ice_storm.add_topping("Caramel Sauce")
        self.assertEqual(str(self.ice_storm), "Ice Storm - Flavor: Chocolate, Size: medium, Toppings: Caramel Sauce, Total: $3.50")

if __name__ == '__main__':
    unittest.main()
