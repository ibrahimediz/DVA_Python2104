from app import create_app
from datetime import datetime
from flask import render_template
import os

# Ortam değişkeninden konfigürasyon adını al
config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_name)

# Template'lerde kullanmak için global değişkenler
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Hata sayfası tanımlaması
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()