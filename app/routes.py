from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Product, Order
from app import db

# Initialize blueprints
main_bp = Blueprint('main', __name__)
mart_bp = Blueprint('mart', __name__, url_prefix='/mart')

# --------------------------
# Main Routes (Auth + Core)
# --------------------------
@main_bp.route('/')
def home():
    featured_products = Product.query.order_by(Product.created_at.desc()).limit(4).all()
    return render_template('index.html', featured_products=featured_products)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.home'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form['email']).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('main.register'))
        
        user = User(
            username=request.form['username'],
            email=request.form['email'],
        )
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

# --------------------------
# Marketplace Routes
# --------------------------
@mart_bp.route('/')
def marketplace():
    products = Product.query.order_by(Product.created_at.desc()).all()
    return render_template('mart/index.html', products=products)

@mart_bp.route('/sell', methods=['GET', 'POST'])
@login_required
def sell_product():
    if request.method == 'POST':
        product = Product(
            title=request.form['title'],
            description=request.form['description'],
            price=float(request.form['price']),
            category=request.form['category'],
            condition=request.form['condition'],
            seller_id=current_user.id
        )
        db.session.add(product)
        db.session.commit()
        flash('Product listed successfully!', 'success')
        return redirect(url_for('mart.marketplace'))
    return render_template('mart/sell.html')

@mart_bp.route('/product/<int:id>')
def view_product(id):
    product = Product.query.get_or_404(id)
    return render_template('mart/product.html', product=product)

@mart_bp.route('/category/<string:category>')
def category_products(category):
    products = Product.query.filter_by(category=category).all()
    return render_template('mart/category.html', products=products, category=category)