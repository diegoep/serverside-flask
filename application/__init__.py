from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_cors import CORS

from application.models import db

application = Flask(__name__, instance_relative_config=True)
CORS(application, resources={r"/*": {"origins": "*"}})

application.config.setdefault('RESTPLUS_MASK_SWAGGER', False)
application.config.from_object('config')

MYSQL = application.config['MYSQL']

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % MYSQL
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['DEBUG'] = False

db.init_app(application)