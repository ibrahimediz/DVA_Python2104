from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import os

# Veritabanu0131 nesnelerini oluu015ftur
db = SQLAlchemy()
mongo = PyMongo()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Konfigu00fcrasyon su0131nu0131fu0131nu0131 yu00fckle
    from app.config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Veritabanu0131 tu00fcru00fcnu00fc belirle
    database_type = app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        # SQLite ayarlaru0131
        db.init_app(app)
    
    elif database_type.lower() == 'mongodb':
        # MongoDB ayarlaru0131
        # Make sure the MongoDB URI is correctly set
        if 'MONGO_URI' not in app.config or not app.config['MONGO_URI']:
            app.logger.error("MongoDB URI is not set properly!")
            raise ValueError("MongoDB URI is not set properly!")
        
        # Set the MongoDB URI directly from the environment variable
        # This ensures we're using the correct connection string for Atlas
        app.config['MONGO_URI'] = os.getenv('MONGO_URI')
        
        # Initialize MongoDB connection
        mongo.init_app(app)
        
        # Verify connection by accessing the database
        with app.app_context():
            try:
                # Check if we can access the database
                mongo.db.command('ping')
                app.logger.info(f"MongoDB connected successfully to Atlas")
                
                # We don't need to create the collection as it should already exist in Atlas
                # Just log the available collections for debugging
                collections = mongo.db.list_collection_names()
                app.logger.info(f"Available collections: {collections}")
                
                if 'books' not in collections:
                    app.logger.warning("'books' collection not found in the database!")
            except Exception as e:
                app.logger.error(f"MongoDB connection error: {str(e)}")
                raise
    
    # Blueprint'leri kayu0131t et
    from app.routes.web import web_bp
    from app.routes.api import api_bp
    
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Veritabanu0131nu0131 oluu015ftur
    with app.app_context():
        if database_type.lower() == 'sqlite':
            db.create_all()
    
    return app