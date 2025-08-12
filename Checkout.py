class Checkout:
    class Discount:
        def __init__(self, num_of_items, price):
            self.num_of_items = num_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price_to_inventory(self, item, price):
        self.prices[item] = price

    def add_item_to_cart(self, item):
        if item not in self.prices:  # item not in inventory
            raise Exception("Bad item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_cart_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)
        return total

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.num_of_items:
                total += self.calculate_item_discounted_total(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

    def calculate_item_discounted_total(self, item, cnt, discount):
        total = 0
        num_of_discounts = cnt // discount.num_of_items
        total += num_of_discounts * discount.price  # discount num of items within range
        remaining = cnt % discount.num_of_items
        total += remaining * self.prices[item]  # remainder of items get regular price
        return total

    def add_discount(self, item, num_of_items, price):
        discount = self.Discount(num_of_items, price)
        self.discounts[item] = discount
