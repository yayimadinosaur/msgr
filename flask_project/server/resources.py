from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', help='Username cannot be blank', required=True)
parser.add_argument('password', help='Password cannot be blank', required=True)

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        return data

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return data

class UserLogoutAccessToken(Resource):
    def post(self):
        data = parser.parse_args()
        return data

class UserLogoutRefreshToken(Resource):
    def post(self):
        data = parser.parse_args()
        return data

class UserTokenRefresh(Resource):
    def post(self):
        data = parser.parse_args()
        return data

class AllRegisteredUsers(Resource):
    def get(self):
        return {
            'message' : 'All registered users'
        }

    def delete(self):
        return {
            'message' : 'Delete all registered users'
        }


class TestResource(Resource):
    def get(self):
        return {
            'message' : 'testing resource'
        }

    