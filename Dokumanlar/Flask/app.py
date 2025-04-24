from app import create_app
from datetime import datetime
from flask import render_template
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ortam deu011fiu015fkeninden konfigu00fcrasyon adu0131nu0131 al
config_name = os.getenv('FLASK_ENV', 'development')
logger.info(f"Starting application with config: {config_name}")

try:
    app = create_app(config_name)
    logger.info("Application created successfully")
    
    # Template'lerde kullanmak iu00e7in global deu011fiu015fkenler
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}
    
    # Hata sayfasu0131 tanu0131mlamasu0131
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
except Exception as e:
    logger.error(f"Error creating application: {str(e)}")
    raise

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)