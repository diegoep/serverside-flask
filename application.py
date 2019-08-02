from flask import Blueprint

from application import application
from application.api.resources.user.user_resource import namespace as users_namespace
from application.api.restplus import api

# jwt = JWT(application, verify, identity)

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
api.add_namespace(users_namespace)
application.register_blueprint(blueprint)

if __name__ == '__main__':
    application.debug = False
    application.run(host='0.0.0.0')
