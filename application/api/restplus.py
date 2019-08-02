from flask_restplus import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(version='1.0', title='DAS-Admin',
          description='An administration application for Data Analytics Service',
          authorizations=authorizations, security='apikey')