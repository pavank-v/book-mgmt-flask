# app.py
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import datetime
from config import Config
from models import db, Book, User

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database and JWT manager
db.init_app(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    # Create a new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Authenticate user
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        # Create a JWT token
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    description = data.get('description')
    published_date = datetime.strptime(data.get('published_date'), '%Y-%m-%d')
    
    # Create a new book
    new_book = Book(title=title, author=author, description=description, published_date=published_date)
    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book added successfully"}), 201

# Get all books with search and pagination functionality
@app.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # If there's a search query, filter the books by title or author
    if search_query:
        books_query = Book.query.filter(
            (Book.title.like(f'%{search_query}%')) | 
            (Book.author.like(f'%{search_query}%'))
        )
    else:
        books_query = Book.query
    
    # Paginate the query
    books_paginated = books_query.paginate(page, per_page, False)
    
    books_data = []
    for book in books_paginated.items:
        books_data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "published_date": book.published_date
        })
    
    return jsonify({
        "books": books_data,
        "total": books_paginated.total,
        "page": page,
        "per_page": per_page,
        "pages": books_paginated.pages
    })

# Get a single book by ID (as before)
@app.route('/books/<int:id>', methods=['GET'])
@jwt_required()
def get_book(id):
    book = Book.query.get_or_404(id)
    book_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "published_date": book.published_date
    }
    return jsonify(book_data)

# Update a book (as before)
@app.route('/books/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.description = data.get('description', book.description)
    book.published_date = data.get('published_date', book.published_date)
    
    db.session.commit()
    
    return jsonify({"msg": "Book updated!"})

# Delete a book (as before)
@app.route('/books/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    
    return jsonify({"msg": "Book deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
