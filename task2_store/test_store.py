"""
Tests for store.py. Run from the workshop folder:

    python task2_store/test_store.py

You do not need to change this file. When every test says PASS, you are done.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from store import Inventory, Cart, OutOfStock


def make_inventory():
    inv = Inventory()
    inv.add_product("apple", 50, 100)
    inv.add_product("pen", 7, 100)
    inv.add_product("laptop", 90000, 1)
    return inv


def test_simple_total():
    cart = Cart(make_inventory())
    cart.add("apple", 3)
    assert cart.total() == 150, f"3 apples at 50 cents should be 150, got {cart.total()}"


def test_new_carts_start_empty():
    inv = make_inventory()
    first = Cart(inv)
    first.add("apple", 2)
    second = Cart(inv)
    assert second.items == {}, f"a brand new cart should be empty, got {second.items}"


def test_remove_all_units():
    cart = Cart(make_inventory())
    cart.add("apple", 2)
    cart.remove("apple", 2)
    assert "apple" not in cart.items, "removing every apple should take apple out of the cart"
    assert cart.item_count() == 0


def test_copy_is_independent():
    cart = Cart(make_inventory())
    cart.add("apple", 1)
    wishlist = cart.copy()
    wishlist.add("pen", 5)
    assert "pen" not in cart.items, "changing the copy should not change the original cart"


def test_bulk_discount_rounds_half_up():
    # 15 pens at 7 cents = 105 cents. 10% of 105 is 10.5 -> rounds UP to 11.
    # So the line costs 105 - 11 = 94 cents.
    cart = Cart(make_inventory())
    cart.add("pen", 15)
    assert cart.total() == 94, f"expected 94, got {cart.total()}"


def test_coupon_after_bulk_and_rounding():
    # 3 apples (150) + 15 pens (94 after bulk) = 244. 25% of 244 = 61 -> 183.
    cart = Cart(make_inventory())
    cart.add("apple", 3)
    cart.add("pen", 15)
    assert cart.total(25) == 183, f"expected 183, got {cart.total(25)}"


def test_coupon_half_cent():
    # 1 apple = 50. 5% of 50 = 2.5 -> rounds UP to 3. Total 47.
    cart = Cart(make_inventory())
    cart.add("apple", 1)
    assert cart.total(5) == 47, f"expected 47, got {cart.total(5)}"


def test_checkout_success():
    inv = make_inventory()
    cart = Cart(inv)
    cart.add("apple", 4)
    assert cart.checkout() == 200
    assert inv.stock["apple"] == 96
    assert cart.items == {}


def test_checkout_failure_changes_nothing():
    inv = make_inventory()
    cart = Cart(inv)
    cart.add("apple", 5)
    cart.add("laptop", 2)  # only 1 laptop in stock
    try:
        cart.checkout()
        assert False, "checkout should have raised OutOfStock"
    except OutOfStock:
        pass
    assert inv.stock["apple"] == 100, (
        f"a failed checkout changed apple stock to {inv.stock['apple']}"
    )


# ---------------------------------------------------------------------------
# Simple test runner (no extra packages needed)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    tests = [(n, f) for n, f in list(globals().items()) if n.startswith("test_")]
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL  {name}: {e}")
        except Exception as e:
            print(f"ERROR {name}: {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed")
    if passed == len(tests):
        print("All tests pass. Impressive!")
