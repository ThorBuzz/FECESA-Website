from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    profile_image = db.Column(db.String(120))
    
    # Relationships
    products = db.relationship('Product', backref='seller', lazy='dynamic', cascade='all, delete-orphan')
    orders = db.relationship('Order', backref='buyer', lazy='dynamic')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(50), nullable=False, index=True)
    condition = db.Column(db.String(50), nullable=False)
    images = db.Column(db.JSON, default=list)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    is_available = db.Column(db.Boolean, default=True)
    
    # Foreign Keys
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    orders = db.relationship('Order', backref='product', lazy='dynamic')
    
    def __repr__(self):
        return f'<Product {self.title}>'

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default='pending', index=True)
    total_amount = db.Column(db.Numeric(10, 2))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    completed_at = db.Column(db.DateTime)
    
    # Foreign Keys
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Additional fields
    payment_method = db.Column(db.String(50))
    shipping_address = db.Column(db.Text)
    transaction_id = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Order {self.id} - {self.status}>'