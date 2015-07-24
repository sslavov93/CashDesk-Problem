class CashDesk():

    def __init__(self):
        self.items = {
            'Sandwich': 2.50, 'Coke': 1.20, 'Custard': 3.20, 'Apple': 0.50,
            'Cucumber': 1.00, 'Noodles': 2.00, 'Magnum': 2.50, 'Soup': 1.60}
        self.meal_deals = [(['Sandwich', 'Coke', 'Apple'], 3.0, [1, 1, 1]),
                           (['Soup', 'Noodles', 'Custard'], 6.50, [1, 2, 1])]
        self.discounts = {'Sandwich': [3, 2], 'Cucumber': [2, 1],
                          'Apple': [4, 3]}
        self.scanned_items = {}
        self.total_price = 0

    def total(self):
        return self.total_price

    def cashout(self):
        self.total_price = 0

    def scan(self, item):
        if item in self.scanned_items and item in self.items:
            self.scanned_items[item] += 1
        elif item in self.items and item not in self.scanned_items:
            self.scanned_items[item] = 1

    def calculate_meal_deals(self):
        for mealdeal in self.meal_deals:
            present = True
            for item in mealdeal[0]:
                if item not in self.scanned_items:
                    present = False
                    break
            if present:
                quantities = []
                for each in self.scanned_items:
                    if each in mealdeal[0]:
                        quantities.append(self.scanned_items[each])
                minq = min(quantities)
                self.total_price += minq * mealdeal[1]
                for each in self.scanned_items:
                    if each in mealdeal[0]:
                        self.scanned_items[each] -= minq

    def calculate_discounts(self):
        for disc_deal in self.scanned_items:
            if disc_deal in self.discounts:
                if (self.scanned_items[disc_deal] >=
                        self.discounts[disc_deal][0]):
                    self.total_price += (
                        self.discounts[disc_deal][1] * self.items[disc_deal])
                    self.scanned_items[
                        disc_deal] -= self.discounts[disc_deal][0]

    def calculate_all(self):
        self.calculate_meal_deals()
        self.calculate_discounts()
        for item in self.scanned_items:
            if self.scanned_items[item] > 0:
                self.total_price += self.items[item]
        return self.total()
