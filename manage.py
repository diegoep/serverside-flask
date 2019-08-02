import datetime

from application import application, db
from application.models import User
from config import DEFAULT_USER
from flask_bcrypt import generate_password_hash
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    "Add seed data to the database."
    check_user = User.query.filter_by(login=DEFAULT_USER['login']).first()
    if (check_user is None):
      user = User(name=DEFAULT_USER['name'], login=DEFAULT_USER['login'], password=generate_password_hash(DEFAULT_USER['password']).decode("utf-8"), email=DEFAULT_USER['email'], userRole=DEFAULT_USER['role'])
      db.session.add(user)
      db.session.commit()

if __name__ == '__main__':
    manager.run()