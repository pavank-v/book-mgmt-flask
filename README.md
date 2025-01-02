# Library Management System API

A RESTful API built with Flask for managing a library system. The API provides functionality for book management with features including user authentication, CRUD operations for books, search capabilities, and pagination.

## Features

- JWT-based authentication
- User registration and login
- Book management (Create, Read, Update, Delete)
- Search functionality for books by title or author
- Pagination support for book listings
- SQLAlchemy ORM for database operations
- Marshmallow schemas for serialization

## Prerequisites

- Python 3.7+
- Flask
- SQLAlchemy
- Flask-JWT-Extended
- Flask-Marshmallow
- PostgreSQL/SQLite (or your preferred database)

## Installation

1. Clone the repository
```bash
git clone https://github.com/pavank-v/book-mgmt-flask
cd book-mgmt-flask
```
2.Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3.Install dependencies
```
pip install -r requirements.txt
```
4.Set up environment variables: Create a .env file in the root directory and add
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=<your-database-url>
JWT_SECRET_KEY=<your-secret-key>
```
5.Initialize the database
```
flask db upgrade
```

## API Endpoints

### Authentication

#### Register a new user
```http
POST /register
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
```
### Login
```http
POST /login
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
```
### Books
- Add a new book
```http
POST /books
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "string",
    "author": "string",
    "description": "string",
    "published_date": "YYYY-MM-DD"
}
```
- Get all books
```http
GET /books?page=1&per_page=10&search=<search_term>
Authorization: Bearer <token>
```
- Get a specific book
```http
GET /books/<id>
Authorization: Bearer <token>
```
- Update a book
```http
PUT /books/<id>
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "string",
    "author": "string",
    "description": "string",
    "published_date": "YYYY-MM-DD"
}
```
- Delete a book
```http
DELETE /books/<id>
Authorization: Bearer <token>
```
## Response Format
- Success Response
```
{
    "message": "Success message",
    "data": {}  // Optional
}
```
- Error Response
```
{
    "message": "Error message"
}
```
- Pagination Response
```
{
    "books": [],
    "total": 0,
    "page": 1,
    "per_page": 10,
    "pages": 1
}
```
## Development
- To run the development server:
```
flask run
```
The API will be available at http://localhost:5000
## Testing
To run tests:
```
python -m pytest
```
## Project Structure
```
book-mgmt-flask/
├── app.py              # Main application file
├── config.py          # Configuration settings
├── models.py          # Database models
├── schemas.py         # Marshmallow schemas
├── requirements.txt   # Project dependencies
└── README.md         # This file
```
## Contributing

- Fork the repository
- Create your feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## Future Enhancements

### Authentication & Security
- Implement password hashing for better security
- Add OAuth2 integration for social login (Google, GitHub)
- Add refresh token mechanism
- Implement role-based access control (Admin, Librarian, Member)
- Add rate limiting for API endpoints

### Book Management
- Add support for book categories/genres
- Implement book image upload and storage
- Add book availability status tracking
- Add book reservation system
- Include book ratings and reviews
- Support for e-book formats and downloads
- Add barcode/ISBN scanning support

### User Features
- Implement user profiles with reading history
- Add favorite books functionality
- Create reading lists/wishlists
- Implement book recommendations based on user history
- Add notification system for due dates/availability

### API Improvements
- Add GraphQL support for flexible querying
- Implement caching for better performance
- Add bulk operations for books
- Implement real-time updates using WebSocket
- Add API versioning
- Implement comprehensive API documentation using Swagger/OpenAPI
- Add request/response compression

### Analytics & Reporting
- Add dashboard for library statistics
- Generate usage reports and analytics
- Track popular books and trends
- Monitor system performance metrics
- Implement audit logging

### Database & Performance
- Add database indexing for improved search performance
- Implement database sharding for scalability
- Add caching layer (Redis/Memcached)
- Optimize query performance
- Implement database backup and recovery system

### Integration
- Add email notification service
- Integrate with payment gateways for fines/fees
- Add support for external book databases
- Implement calendar integration for events/due dates
- Add printing service integration

### Infrastructure
- Containerize application using Docker
- Set up CI/CD pipeline
- Implement automated testing
- Add monitoring and logging system
- Set up load balancing
- Implement automatic backups

### Mobile Support
- Create mobile-friendly API endpoints
- Add push notifications support
- Implement offline capabilities
- Add location-based services

### Administrative Features
- Add comprehensive admin dashboard
- Implement reporting tools
- Add user management system
- Create inventory management system
- Add financial tracking features
