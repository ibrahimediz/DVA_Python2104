from app import db
import datetime

class Book(db.Model):
    """Kitap modeli - SQLite için"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    publication_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<Book {self.title}>'
    
    def to_dict(self):
        """Model verilerini sözlük olarak döndür (API için)"""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'price': self.price,
            'publication_date': self.publication_date.isoformat() if self.publication_date else None,
            'created_at': self.created_at.isoformat()
        }


def create_book_mongodb(mongo, book_data):
    """MongoDB için kitap oluşturma fonksiyonu"""
    if mongo is None:
        raise ValueError("MongoDB connection is not initialized properly")
    
    # MongoDB Atlas'taki dva2104 veritabanının books koleksiyonunu kullan
    # Otomatik ID oluştur
    last_book = mongo.db.books.find_one(sort=[('id', -1)])
    new_id = 1
    if last_book and 'id' in last_book:
        new_id = last_book['id'] + 1
    
    book_data['id'] = new_id
    book_data['created_at'] = datetime.datetime.utcnow()
    
    # books koleksiyonuna ekle
    return mongo.db.books.insert_one(book_data)


def get_books_mongodb(mongo):
    """MongoDB'den tüm kitapları getir"""
    if mongo is None or mongo.db is None:
        raise ValueError("MongoDB connection is not initialized properly")
    
    # MongoDB Atlas'taki dva2104 veritabanının books koleksiyonundan tüm kitapları getir
    return list(mongo.db.books.find({}, {'_id': 0}))


def get_book_mongodb(mongo, book_id):
    """MongoDB'den belirli bir kitabı getir"""
    if mongo is None or mongo.db is None:
        raise ValueError("MongoDB connection is not initialized properly")
    
    # MongoDB Atlas'taki dva2104 veritabanının books koleksiyonundan belirli bir kitabı getir
    return mongo.db.books.find_one({'id': int(book_id)}, {'_id': 0})