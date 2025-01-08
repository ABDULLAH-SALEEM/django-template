import bcrypt
import jwt
from django.conf import settings
from .models import User

# Add your secret key in settings.py


class AuthService:
    @staticmethod
    def _hash_password(password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    @staticmethod
    def generate_token(user_id):
        return jwt.encode({"user_id": user_id}, settings.SECRET_KEY, algorithm="HS256")

    @staticmethod
    def decode_token(token):
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

    @staticmethod
    def get_user_by_email(email):
        return User.objects.filter(email=email).first()

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def create_user(name, email, password):
        hashed_password = AuthService._hash_password(password)
        return User.objects.create(name=name, email=email, password=hashed_password)

    @staticmethod
    def verify_user_credentials(email, password):
        user = AuthService.get_user_by_email(email)
        if user and AuthService._check_password(password, user.password):
            return user
        return None

    @staticmethod
    def generate_user_token(user):
        return AuthService._generate_token(user.id)

    @staticmethod
    def decode_user_token(token):
        return AuthService._decode_token(token)
