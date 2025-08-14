from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES

db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, photos)
    
    # Register blueprints
    from app.routes import main_bp, mart_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(mart_bp, url_prefix='/mart')
    
    return app