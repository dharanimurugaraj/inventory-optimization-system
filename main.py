from inventory import Inventory, Product
from order_system import Order, OrderQueue
from demand_prediction import predict_demand
from replenishment import optimize_restock

# Setup
inventory = Inventory()
orders = OrderQueue()

# Add sample products
inventory.add_product(Product("SKU123", "iPhone", "Electronics", 10))
inventory.add_product(Product("SKU124", "MacBook", "Electronics", 2))

# Add orders
orders.add_order(Order("ORD001", "SKU124", 1, priority=1))

# Process orders
next_order = orders.process_next()
if next_order:
    product = inventory.get_product_by_sku(next_order.sku)
    if product and product.stock >= next_order.quantity:
        inventory.update_stock(product.sku, -next_order.quantity)
        print(f"Processed order: {next_order.order_id}")
    else:
        print("Out of stock!")

# Predict demand and restock
sales_history = [2, 3, 5, 6, 4, 7]  # Dummy data
predicted = predict_demand(sales_history)
restock = optimize_restock(inventory.get_product_by_sku("SKU124").stock, predicted)
print(f"Restock needed for SKU124: {restock}")
