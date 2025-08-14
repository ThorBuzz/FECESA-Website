import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    # Required variables
    SECRET_KEY = os.getenv('d2e6f2808c9620c1af47f25043ce3f6968a1883e82d3d9e227cb886e653e2367')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    
    # Optional variables with defaults
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/static/uploads')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'