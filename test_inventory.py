from inventory import Inventory, Product

def test_inventory_lookup():
    inv = Inventory()
    p = Product("SKU1", "Watch", "Wearable", 10)
    inv.add_product(p)
    assert inv.get_product_by_sku("SKU1") == p

test_inventory_lookup()
print("All tests passed.")
