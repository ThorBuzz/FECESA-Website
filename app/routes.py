from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Product, Order
from app.forms import ProductForm
from app import db, photos

# Main Blueprint (for auth and core pages)
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form
        pass
    return render_template('contact.html')

# Authentication routes (login, register, logout) go here...

# Mart Blueprint (for marketplace)
mart_bp = Blueprint('mart', __name__)

@mart_bp.route('/')
def marketplace():
    products = Product.query.order_by(Product.created_at.desc()).limit(8).all()
    return render_template('mart/index.html', products=products)

@mart_bp.route('/sell', methods=['GET', 'POST'])
@login_required
def sell_product():
    form = ProductForm()
    if form.validate_on_submit():
        # Handle product creation
        pass
    return render_template('mart/sell.html', form=form)

# Other mart routes...