from flask_marshmallow import Marshmallow
from models import Book, User

ma = Marshmallow()

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
