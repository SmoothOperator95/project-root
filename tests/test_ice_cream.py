# test_ice_cream.py
import unittest
from api.ice_cream import IceCream

class TestIceCream(unittest.TestCase):
    def test_add_flavor(self):
        ice_cream = IceCream()
        ice_cream.add_flavor("Chocolate")
        self.assertEqual(ice_cream.get_num_flavors(), 1)
    
    def test_get_total(self):
        ice_cream = IceCream()
        ice_cream.add_flavor("Chocolate")
        ice_cream.add_flavor("Vanilla Bean")
        self.assertEqual(ice_cream.get_total(), 6.00)

if __name__ == "__main__":
    unittest.main()
