from flask import Blueprint, request

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():
    response = {
        'results': 'get_users'
    }
    return response
