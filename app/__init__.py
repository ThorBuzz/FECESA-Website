# Add this at the top of the file
# type: ignore
from flask_reuploaded import UploadSet, configure_uploads, IMAGES
from flask_migrate import Migrate
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_reuploaded import UploadSet, configure_uploads, IMAGES  # Updated import

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main_bp.login'  # Specify login route
photos = UploadSet('photos', IMAGES)       # Configure upload set

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-key-123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(app.root_path, 'static/uploads')
    app.config['UPLOADED_PHOTOS_ALLOW'] = ['jpg', 'png', 'jpeg', 'gif']
    
    # Create upload folder if needed
    os.makedirs(app.config['UPLOADED_PHOTOS_DEST'], exist_ok=True)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, photos)  # Now using flask-reuploaded
    
    # Register blueprints
    from app.routes import main_bp, mart_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(mart_bp, url_prefix='/mart')
    
    return app