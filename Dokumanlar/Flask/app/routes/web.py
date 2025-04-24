from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from app.models.book import Book, create_book_mongodb, get_books_mongodb, get_book_mongodb
from app import db, mongo
from datetime import datetime

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    """Ana sayfa"""
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        books = Book.query.all()
    else:  # MongoDB
        books = get_books_mongodb(mongo)
    
    return render_template('index.html', books=books, db_type=database_type)

@web_bp.route('/book/new', methods=['GET', 'POST'])
def new_book():
    """Yeni kitap ekleme sayfasu0131"""
    if request.method == 'POST':
        # Form verilerini al
        title = request.form.get('title')
        author = request.form.get('author')
        description = request.form.get('description')
        price = float(request.form.get('price', 0))
        pub_date_str = request.form.get('publication_date')
        
        # Tarih formatu0131nu0131 kontrol et
        publication_date = None
        if pub_date_str:
            try:
                publication_date = datetime.strptime(pub_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Geu00e7ersiz tarih formatu0131! Lu00fctfen YYYY-MM-DD formatu0131nda girin.', 'danger')
                return render_template('new_book.html')
        
        database_type = current_app.config['DATABASE_TYPE']
        
        if database_type.lower() == 'sqlite':
            # SQLite iu00e7in yeni kitap oluu015ftur
            new_book = Book(
                title=title,
                author=author,
                description=description,
                price=price,
                publication_date=publication_date
            )
            db.session.add(new_book)
            db.session.commit()
        else:  # MongoDB
            # MongoDB iu00e7in yeni kitap oluu015ftur
            book_data = {
                'title': title,
                'author': author,
                'description': description,
                'price': price,
                'publication_date': pub_date_str if pub_date_str else None
            }
            create_book_mongodb(mongo, book_data)
        
        flash('Kitap bau015faru0131yla eklendi!', 'success')
        return redirect(url_for('web.index'))
    
    return render_template('new_book.html')

@web_bp.route('/book/<int:book_id>')
def view_book(book_id):
    """Kitap detay sayfasu0131"""
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        book = Book.query.get_or_404(book_id)
    else:  # MongoDB
        book = get_book_mongodb(mongo, book_id)
        if not book:
            return render_template('404.html'), 404
    
    return render_template('view_book.html', book=book)

@web_bp.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    """Kitap du00fczenleme sayfasu0131"""
    database_type = current_app.config['DATABASE_TYPE']
    
    # Kitabu0131 getir
    if database_type.lower() == 'sqlite':
        book = Book.query.get_or_404(book_id)
    else:  # MongoDB
        book = get_book_mongodb(mongo, book_id)
        if not book:
            return render_template('404.html'), 404
    
    if request.method == 'POST':
        # Form verilerini al
        title = request.form.get('title')
        author = request.form.get('author')
        description = request.form.get('description')
        price = float(request.form.get('price', 0))
        pub_date_str = request.form.get('publication_date')
        
        # Tarih formatu0131nu0131 kontrol et
        publication_date = None
        if pub_date_str:
            try:
                publication_date = datetime.strptime(pub_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Geu00e7ersiz tarih formatu0131! Lu00fctfen YYYY-MM-DD formatu0131nda girin.', 'danger')
                return render_template('edit_book.html', book=book)
        
        if database_type.lower() == 'sqlite':
            # SQLite iu00e7in kitabu0131 gu00fcncelle
            book.title = title
            book.author = author
            book.description = description
            book.price = price
            book.publication_date = publication_date
            db.session.commit()
        else:  # MongoDB
            # MongoDB iu00e7in kitabu0131 gu00fcncelle
            update_data = {
                'title': title,
                'author': author,
                'description': description,
                'price': price,
                'publication_date': pub_date_str if pub_date_str else None
            }
            mongo.db.books.update_one({'id': int(book_id)}, {'$set': update_data})
        
        flash('Kitap bau015faru0131yla gu00fcncellendi!', 'success')
        return redirect(url_for('web.view_book', book_id=book_id))
    
    return render_template('edit_book.html', book=book)

@web_bp.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    """Kitap silme iu015flemi"""
    database_type = current_app.config['DATABASE_TYPE']
    
    if database_type.lower() == 'sqlite':
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
    else:  # MongoDB
        result = mongo.db.books.delete_one({'id': int(book_id)})
        if result.deleted_count == 0:
            flash('Kitap bulunamadu0131!', 'danger')
            return redirect(url_for('web.index'))
    
    flash('Kitap bau015faru0131yla silindi!', 'success')
    return redirect(url_for('web.index'))