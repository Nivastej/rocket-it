from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'


products = [
    {
        'id': 1,
        'name': 'Apple',
        'price': 0.5,
        'image': 'apple.jpg'
    },
    {
        'id': 2,
        'name': 'Banana',
        'price': 0.3,
        'image': 'banana.jpg'
    },
    {
        'id': 3,
        'name': 'Carrot',
        'price': 0.4,
        'image': 'carrot.jpg'
    },
]


@app.route('/')
def home():
    return render_template('home.html', products=products)


@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((item for item in products if item['id'] == product_id),
                   None)
    return render_template('product.html', product=product)


@app.route('/cart')
def cart():
    if 'cart' not in session:
        session['cart'] = []
    return render_template('cart.html', cart=session['cart'])


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((item for item in products if item['id'] == product_id),
                   None)
    if product:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
    return redirect(url_for('cart'))


@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return "Checkout completed!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
