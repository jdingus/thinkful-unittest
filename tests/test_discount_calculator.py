import sys
sys.path.insert(0, '../')
from calculate_discount import calculate_discount

import unittest

class CalculateDiscountTests(unittest.TestCase):
    def testDiscountNormal(self):
        sale_price = calculate_discount(200,10,30)

        # Check that the right values are returned
        self.assertEqual(sale_price, 150)
				
    def testPriceZero(self):
        sale_price = calculate_discount(0,10,30)

        # Check that the right values are returned
        self.assertEqual(sale_price, 0)

    def testPriceNegative(self):
        with self.assertRaises(Exception):
            sale_price = calculate_discount(-10,10,30)
						
if __name__ == "__main__":
    unittest.main()