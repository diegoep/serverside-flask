from flask_restplus import Resource, fields
from application.api.restplus import api
from flask_jwt import jwt_required
from flask import request, abort
from application.serialize import Serializer
from application.api.resources.user.user_service import UserService

namespace = api.namespace('users', description='Operations related to users')
user_post = api.model('User Post', {
    'email': fields.String(required=True, description='Email', max_length=80),
    'login': fields.String(required=True, description='Login', max_length=20),
    'name': fields.String(required=True, description='Name', max_length=80),
    'userRole': fields.String(required=True, enum=['ROLE_USER', 'ROLE_ADMIN']),
    'password': fields.String(required=True, description='Password', max_length=250)
})
user_get = api.model('User Get', {
    'id': fields.Integer,
    'email': fields.String,
    'login': fields.String,
    'name': fields.String,
    'userRole': fields.String(enum=['ROLE_USER', 'ROLE_ADMIN'])
})

@namespace.route('')
class UserCollection(Resource):

    # @jwt_required()
    @api.marshal_with(user_get)
    def get(self):
        """Return list of users"""
        releases = UserService.get_all()
        return Serializer.serialize_list(releases)

    # @jwt_required()
    @api.expect(user_post)
    @api.response(201, 'User post successfully created.')
    @api.marshal_with(user_get)
    def post(self):
        """Create a new user"""
        if not request.json or "name" not in request.json or "login" not in request.json or "password" not in request.json or "email" not in request.json or "userRole" not in request.json:
            abort(400)

        user = UserService.create(request.json)

        return user.serialize()

    # @jwt_required()
    @api.expect(user_post)
    @api.marshal_with(user_get)
    def put(self):
        """Update the user"""
        if not request.json or "id" not in request.json:
            abort(400)

        id = request.json['id']

        user = UserService.get_by_id(id)
        user = UserService.update(user, request.json)

        return user.serialize()

@namespace.route('/<int:id>')
@api.response(404, 'User not found.')
@namespace.param('id', 'The user id')
class UserItem(Resource):

    # @jwt_required()
    @api.marshal_with(user_get)
    def get(self, id):
        """Return a user"""
        user = UserService.get_by_id(id)
        return user.serialize()

    # @jwt_required()
    def delete(self, id):
        """Delete a user"""
        user = UserService.get_by_id(id)
        UserService.delete(user)

        return {"result": True}
