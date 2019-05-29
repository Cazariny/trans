from tan import db
import random
import string
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)


secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits)
                     for x in xrange(32))


class User(db.Base):
    """
    Registered user information is stored in db
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True)
    picture = db.Column(db.String)
    email = db.Column(db.String)

    @staticmethod
    def verify_auth_token(token):
        """
         Gets a token for the user login
        """
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            # Valid Token, but expired
            return None
        except BadSignature:
            # Invalid Token
            return None
        user_id = data['id']
        return user_id


class Datos(db.Base):
    """
    Registered categories information is stored in db
    """
    __tablename__ = 'documentos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), index=True)
    url = db.Column(db.Integer, db.ForeignKey('user.id'))

class documentos(db.Base):
    """
    Registered items information is stored in db
    """
    __tablename__ = 'items'
    name = db.Column(db.String(400), nullable=False)
