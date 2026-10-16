"""
A small online store: an inventory and shopping carts.

All money is stored in CENTS as whole numbers (int), so $12.50 is 1250.

Pricing rules (read carefully, the tests check them exactly):
  1. Line total = price * quantity.
  2. Bulk discount: if a line has 10 or more of the same item,
     that line gets 10% off.
  3. Subtotal = sum of all line totals after bulk discounts.
  4. Coupon: a percent-off coupon is applied to the subtotal,
     AFTER bulk discounts.
  5. Every discount is rounded to the nearest cent, and exact halves
     round UP (10.5 cents -> 11 cents). This is "round half up".

Checkout rules:
  - Checkout must either succeed completely or change nothing.
    If any item does not have enough stock, raise OutOfStock and
    leave the inventory exactly as it was.

This file has 5 bugs. Some of them do not show up until you use the code
in a specific way.
"""


class OutOfStock(Exception):
    pass


class Inventory:
    def __init__(self):
        self.prices = {}   # name -> price in cents
        self.stock = {}    # name -> units available

    def add_product(self, name, price_cents, units):
        self.prices[name] = price_cents
        self.stock[name] = self.stock.get(name, 0) + units


def percent_off(amount_cents, percent):
    """Return the discount in cents, rounded to the nearest cent."""
    return round(amount_cents * percent / 100)


class Cart:
    def __init__(self, inventory, items={}):
        self.inventory = inventory
        self.items = items  # name -> quantity

    def add(self, name, qty=1):
        if name not in self.inventory.prices:
            raise KeyError(f"unknown product: {name}")
        self.items[name] = self.items.get(name, 0) + qty

    def remove(self, name, qty=1):
        """Remove qty units. If none are left, the item leaves the cart."""
        self.items[name] -= qty
        if self.items[name] < 0:
            del self.items[name]

    def item_count(self):
        """Number of different products in the cart."""
        return len(self.items)

    def copy(self):
        """Return an independent copy of this cart (e.g. a saved wishlist)."""
        return Cart(self.inventory, self.items)

    def total(self, coupon_percent=0):
        subtotal = 0
        for name, qty in self.items.items():
            line = self.inventory.prices[name] * qty
            if qty >= 10:
                line -= percent_off(line, 10)
            subtotal += line
        return subtotal - percent_off(subtotal, coupon_percent)

    def checkout(self, coupon_percent=0):
        """Charge the cart: reduce stock and return the total in cents."""
        for name, qty in self.items.items():
            if self.inventory.stock.get(name, 0) < qty:
                raise OutOfStock(name)
            self.inventory.stock[name] -= qty
        amount = self.total(coupon_percent)
        self.items = {}
        return amount


if __name__ == "__main__":
    inv = Inventory()
    inv.add_product("notebook", 350, 100)
    inv.add_product("pen", 125, 500)

    cart = Cart(inv)
    cart.add("notebook", 2)
    cart.add("pen", 12)
    print("Total with 15% coupon:", cart.total(15), "cents")
