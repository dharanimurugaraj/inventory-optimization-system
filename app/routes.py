from flask import Blueprint, render_template, request
from inventory import Inventory, Product
from order_system import Order, OrderQueue
from demand_prediction import predict_demand
from replenishment import optimize_restock

main = Blueprint('main', __name__)

inventory = Inventory()
orders = OrderQueue()

# Dummy data
inventory.add_product(Product("SKU123", "iPhone", "Electronics", 10))
inventory.add_product(Product("SKU124", "MacBook", "Electronics", 2))

@main.route('/')
def index():
    products = inventory.products.values()
    return render_template('index.html', products=products)

@main.route('/restock/<sku>')
def restock(sku):
    product = inventory.get_product_by_sku(sku)
    sales_history = [2, 3, 5, 6, 4, 7]  # Dummy
    predicted = predict_demand(sales_history)
    restock_amount = optimize_restock(product.stock, predicted)
    inventory.update_stock(sku, restock_amount)
    return f"Restocked {product.name} by {restock_amount}. New stock: {product.stock}"

from flask import flash, redirect, url_for

@main.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        sku = request.form['sku']
        category = request.form['category']
        stock = int(request.form['stock'])
        inventory.add_product(Product(sku, name, category, stock))
        flash(f'Product {name} added!')
        return redirect(url_for('main.index'))
    return render_template('add_product.html')
