class Product:
    def __init__(self, sku, name, category, stock):
        self.sku = sku
        self.name = name
        self.category = category
        self.stock = stock

class Inventory:
    def __init__(self):
        self.products = {}  # Hash table: SKU → Product

    def add_product(self, product):
        self.products[product.sku] = product

    def get_product_by_sku(self, sku):
        return self.products.get(sku)

    def get_products_by_category(self, category):
        return [p for p in self.products.values() if p.category == category]

    def update_stock(self, sku, delta):
        if sku in self.products:
            self.products[sku].stock += delta
