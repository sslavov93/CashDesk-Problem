import unittest
from cash_desk import CashDesk


class TestCashDesk(unittest.TestCase):

    def setUp(self):
        self.kasa = CashDesk()
        self.kasa.scan('Sandwich')

    def test_init(self):
        self.assertEqual(
            self.kasa.discounts,
            {'Sandwich': [3, 2], 'Cucumber': [2, 1], 'Apple': [4, 3]})
        self.assertEqual(
            self.kasa.meal_deals,
            [(['Sandwich', 'Coke', 'Apple'], 3.0, [1, 1, 1]),
             (['Soup', 'Noodles', 'Custard'], 6.50, [1, 2, 1])])

    def test_scan_with_present_item(self):
        self.kasa.scan('Sandwich')
        self.assertEqual(self.kasa.scanned_items, {'Sandwich': 2})

    def test_scan_with_new_valid_item(self):
        self.kasa.scan('Apple')
        self.assertEqual(self.kasa.scanned_items,
                         {'Sandwich': 1, 'Apple': 1})

    def test_scan_with_new_invalid_item(self):
        self.kasa.scan('asd')
        self.assertEqual(self.kasa.scanned_items, {'Sandwich': 1})

    def test_total_method(self):
        result = self.kasa.total()
        self.assertEqual(result, 0)

    def test_calculate_meal_with_missing_item(self):
        self.kasa.scanned_items = {'Apple': 2}
        self.kasa.calculate_meal_deals()
        self.assertEqual(self.kasa.total_price, 0)

    def test_calculate_discounts(self):
        self.kasa.scanned_items = {'Soup': 2}
        self.kasa.calculate_discounts()
        self.assertEqual(self.kasa.total_price, 0)

    def test_calculate_all(self):
        result = self.kasa.calculate_all()
        self.assertEqual(result, 2.50)

    def test_cashout(self):
        self.assertEqual(self.kasa.total_price, 0)

if __name__ == "__main__":
    unittest.main()
