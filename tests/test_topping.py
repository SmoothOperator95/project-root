# test_topping.py
import unittest
from api.topping import Topping

class TestTopping(unittest.TestCase):

    def test_valid_topping(self):
        # Test creating a valid topping
        topping = Topping("Caramel Sauce")
        self.assertEqual(topping.topping, "Caramel Sauce")
        self.assertEqual(topping.get_total(), 0.50)
        
    def test_invalid_topping(self):
        # Test creating an invalid topping (should raise ValueError)
        with self.assertRaises(ValueError):
            Topping("Invalid Topping")
    
    def test_multiple_toppings(self):
        # Test creating multiple toppings and calculating their total
        topping1 = Topping("Caramel Sauce")
        topping2 = Topping("Storios")
        topping3 = Topping("Whipped Cream")
        
        self.assertEqual(topping1.get_total(), 0.50)
        self.assertEqual(topping2.get_total(), 1.00)
        self.assertEqual(topping3.get_total(), 0.00)
        
    def test_str_method(self):
        # Test the __str__ method of the Topping class
        topping = Topping("Chocolate Sauce")
        self.assertEqual(str(topping), "Chocolate Sauce - $0.50")

if __name__ == "__main__":
    unittest.main()
