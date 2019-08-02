import datetime
import os

DEBUG = False
JWT_SECRET_KEY = 'super-secret'
JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)
JWT_AUTH_HEADER_PREFIX = 'Bearer'

MYSQL={
    'user': os.environ['RDS_USERNAME'],
    'pw': os.environ['RDS_PASSWORD'],
    'db': os.environ['RDS_DB_NAME'],
    'host': os.environ['RDS_HOSTNAME'],
    'port': os.environ['RDS_PORT']
}

DEFAULT_USER = {
    'name' : 'admin',
    'login' : 'admin',
    'password' : 'admin',
    'email' : 'admin@admin',
    'role' : 'ROLE_ADMIN'
}

ACCESS_KEY = {
    'expirationHours' : 1,
    'salt' : 'DEFAULT_SECRET'
}