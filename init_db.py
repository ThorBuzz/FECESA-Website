# Add this at the top of the file
# type: ignore
from flask_reuploaded import UploadSet, configure_uploads, IMAGES
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_reuploaded import UploadSet, configure_uploads, IMAGES  # Updated import

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
photos = UploadSet('photos', IMAGES)  # Configure file uploads

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/uploads'  # Upload folder path
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for file uploads
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    configure_uploads(app, photos)  # Enable file uploads
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app

# Import models (at bottom to prevent circular imports)
from app.models import User, Product, Order