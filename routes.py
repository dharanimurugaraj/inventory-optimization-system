from flask import Blueprint, render_template, request, redirect, url_for, flash
from supabase_client import supabase

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = supabase.table('products').select("*").execute()
    products = data.data
    return render_template('index.html', products=products)

@main.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        sku = request.form['sku']
        name = request.form['name']
        category = request.form['category']
        stock = int(request.form['stock'])

        supabase.table('products').insert({
            "sku": sku,
            "name": name,
            "category": category,
            "stock": stock
        }).execute()

        flash("Product added successfully.")
        return redirect(url_for('main.index'))
    return render_template('add_product.html')
