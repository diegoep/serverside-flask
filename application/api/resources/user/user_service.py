from application.models import db, User
from application.utils import find_or_404
from flask_bcrypt import generate_password_hash


class UserService:

    def get_all():
        return User.query.all()

    def get_by_id(id):
        return find_or_404(User, id)

    def create(body):
        user = User()
        user.name = body.get("name")
        user.login = body.get("login")
        user.password = generate_password_hash(body.get("password")).decode('utf-8')
        user.email = body.get("email")
        user.userRole = body.get("userRole")

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        return user

    def update(user, body):
        user.name = body.get("name", user.name)
        user.login = body.get("login", user.login)
        user.password = generate_password_hash(body.get("password", user.password)).decode('utf-8')
        user.email = body.get("email", user.email)
        user.userRole = body.get("userRole", user.userRole)

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        return user

    def delete(user):
        db.session.delete(user)
        db.session.commit()
