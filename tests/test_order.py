# test_order.py
import unittest
from api.order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        order = Order()
        order.add_flavor("Chocolate")
        order.add_flavor("Mint Chocolate Chip")
        order.add_topping("Caramel Sauce")
        
        self.assertEqual(order.get_num_flavors(), 2)
        self.assertEqual(order.get_size(), 2)
        self.assertEqual(order.get_total(), 4.50)  # 3.00 (Chocolate) + 4.00 (Mint Chocolate Chip) + 0.50 (Caramel Sauce)
        self.assertIn("Chocolate Ice Cream - $3.00", str(order))
        self.assertIn("Mint Chocolate Chip Ice Cream - $4.00", str(order))
        self.assertIn("Caramel Sauce - $0.50", str(order))

if __name__ == "__main__":
    unittest.main()
