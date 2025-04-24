import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class Config:
    """Uygulama konfigürasyon sınıfı"""
    # Flask ayarları
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    
    # Veritabanı ayarları
    DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'sqlite')
    
    # SQLite ayarları
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getenv('SQLITE_DATABASE', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # MongoDB ayarları
    # MongoDB Atlas URI'sini doğrudan .env dosyasından al
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/dva2104')
    
    # dva2104 veritabanı adını doğrudan belirt
    MONGO_DBNAME = 'dva2104'
    
    @staticmethod
    def init_app(app):
        """Uygulama için ek konfigürasyon ayarları"""
        pass


class DevelopmentConfig(Config):
    """Geliştirme ortamı konfigürasyonu"""
    DEBUG = True


class ProductionConfig(Config):
    """Üretim ortamı konfigürasyonu"""
    DEBUG = False
    # Üretim ortamında daha güvenli ayarlar
    # Örneğin: SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    """Test ortamı konfigürasyonu"""
    TESTING = True
    # Test için geçici veritabanı
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Konfigürasyon sözlüğü
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}