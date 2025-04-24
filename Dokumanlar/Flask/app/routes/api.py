from flask import Blueprint, jsonify, request, current_app
from app.models.book import Book, create_book_mongodb, get_books_mongodb, get_book_mongodb
from app import db, mongo
from datetime import datetime

api_bp = Blueprint('api', __name__)

@api_bp.route('/books', methods=['GET'])
def get_books():
    """Tu00fcm kitaplaru0131 listele"""
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        books = Book.query.all()
        return jsonify({
            'success': True,
            'data': [book.to_dict() for book in books],
            'count': len(books)
        })
    else:  # MongoDB
        books = get_books_mongodb(mongo)
        return jsonify({
            'success': True,
            'data': books,
            'count': len(books)
        })

@api_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Belirli bir kitabu0131 getir"""
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'success': False, 'error': 'Kitap bulunamadu0131'}), 404
        return jsonify({'success': True, 'data': book.to_dict()})
    else:  # MongoDB
        book = get_book_mongodb(mongo, book_id)
        if not book:
            return jsonify({'success': False, 'error': 'Kitap bulunamadu0131'}), 404
        return jsonify({'success': True, 'data': book})

@api_bp.route('/books', methods=['POST'])
def create_book():
    """Yeni kitap oluu015ftur"""
    data = request.get_json()
    
    if not data or not all(key in data for key in ['title', 'author', 'price']):
        return jsonify({
            'success': False,
            'error': 'Eksik bilgi. Bau015flu0131k, yazar ve fiyat zorunludur.'
        }), 400
    
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        # SQLite iu00e7in yeni kitap oluu015ftur
        publication_date = None
        if 'publication_date' in data and data['publication_date']:
            try:
                publication_date = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': 'Geu00e7ersiz tarih formatu0131! Lu00fctfen YYYY-MM-DD formatu0131nda girin.'
                }), 400
        
        new_book = Book(
            title=data['title'],
            author=data['author'],
            description=data.get('description'),
            price=float(data['price']),
            publication_date=publication_date
        )
        db.session.add(new_book)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Kitap bau015faru0131yla eklendi',
            'data': new_book.to_dict()
        }), 201
    else:  # MongoDB
        # MongoDB iu00e7in yeni kitap oluu015ftur
        book_data = {
            'title': data['title'],
            'author': data['author'],
            'description': data.get('description'),
            'price': float(data['price']),
            'publication_date': data.get('publication_date')
        }
        result = create_book_mongodb(mongo, book_data)
        
        return jsonify({
            'success': True,
            'message': 'Kitap bau015faru0131yla eklendi',
            'data': book_data
        }), 201

@api_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """Kitap gu00fcncelle"""
    data = request.get_json()
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'success': False, 'error': 'Kitap bulunamadu0131'}), 404
        
        # Gu00fcncellenecek alanlar
        if 'title' in data:
            book.title = data['title']
        if 'author' in data:
            book.author = data['author']
        if 'description' in data:
            book.description = data['description']
        if 'price' in data:
            book.price = float(data['price'])
        if 'publication_date' in data and data['publication_date']:
            try:
                book.publication_date = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': 'Geu00e7ersiz tarih formatu0131! Lu00fctfen YYYY-MM-DD formatu0131nda girin.'
                }), 400
        
        db.session.commit()
        return jsonify({'success': True, 'data': book.to_dict()})
    else:  # MongoDB
        # MongoDB iu00e7in gu00fcncelleme iu015flemi
        update_data = {}
        if 'title' in data:
            update_data['title'] = data['title']
        if 'author' in data:
            update_data['author'] = data['author']
        if 'description' in data:
            update_data['description'] = data['description']
        if 'price' in data:
            update_data['price'] = float(data['price'])
        if 'publication_date' in data:
            update_data['publication_date'] = data['publication_date']
        
        result = mongo.db.books.update_one({'id': int(book_id)}, {'$set': update_data})
        if result.matched_count == 0:
            return jsonify({'success': False, 'error': 'Kitap bulunamadu0131'}), 404
        
        updated_book = get_book_mongodb(mongo, book_id)
        return jsonify({'success': True, 'data': updated_book})

@api_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Kitap sil"""
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'success': False, 'error': 'Kitap bulunamadu0131'}), 404
        
        db.session.delete(book)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Kitap bau015faru0131yla silindi'})
    else:  # MongoDB
        result = mongo.db.books.delete_one({'id': int(book_id)})
        if result.deleted_count == 0:
            return jsonify({'success': False, 'error': 'Kitap bulunamadu0131'}), 404
        
        return jsonify({'success': True, 'message': 'Kitap bau015faru0131yla silindi'})