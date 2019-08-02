from application.models import User
from flask_bcrypt import check_password_hash
from flask import abort, jsonify, make_response

def verify(username, password):
    if not (username and password):
        return False
    try:
      user = User.query.filter_by(login=username).first()
    except Exception as e:
      abort(make_response(jsonify(description="error.database.connection"), 500))
    if (user is None):
      return False
    if check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return user_id
