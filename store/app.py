from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'such_a_very_secret_key_for_this_demo_project'

# Dummy user for demonstration purposes
USER_DATA = {
    "username": "testuser",
    "password": "password123"
}

# Dummy product data
PRODUCTS = [
    {"id": 1, "name": "Product 1", "description": "This is product 1."},
    {"id": 2, "name": "Product 2", "description": "This is product 2."}
]

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('product_listing'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_DATA['username'] and password == USER_DATA['password']:
            session['logged_in'] = True
            return redirect(url_for('product_listing'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/product_listing')
def product_listing():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('product_listing.html', products=PRODUCTS)

@app.route('/product_details/<int:product_id>')
def product_details(product_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    product = next((product for product in PRODUCTS if product["id"] == product_id), None)
    if product is None:
        return "Product not found."
    return render_template('product_details.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    cart = session.get('cart', {})
    
    product_id_str = str(product_id)  # Ensure the product ID is a string.
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    session['cart'] = cart  # Update the session with the modified cart.
    session.modified = True  # Ensure the modification is marked.
    
    return redirect(url_for('product_listing'))


@app.route('/view_cart')
def view_cart():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    cart_products = []
    cart = session.get('cart', {})
    for product_id_str, quantity in cart.items():
        product = next((product for product in PRODUCTS if str(product["id"]) == product_id_str), None)
        if product:
            product['quantity'] = quantity  # Add quantity to the product dict
            cart_products.append(product)
    return render_template('view_cart.html', cart_products=cart_products)


if __name__ == '__main__':
    app.run(debug=True)
