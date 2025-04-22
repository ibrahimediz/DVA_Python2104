import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','Gizli Kimseye Söyleme')
    DEBUG= os.getenv("DEBUG","False")