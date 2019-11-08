from flask import Blueprint, request

subject = Blueprint('subject', __name__)

@subject.route('/', methods=['GET'])
def get_subjects():
    response = {
        'results': 'get_subjects'
    }
    return response

@subject.route('/', methods=['POST'])
def create_subject():
    response = {
        'results': 'create_subject'
    }
    return response

@subject.route('/<sub_id>', methods=['GET'])
def get_subject(sub_id):
    response = {
        'results': 'get_subject_{}'.format(sub_id)
    }
    return response

@subject.route('/<sub_id>', methods=['POST'])
def edit_subject(sub_id):
    response = {
        'results': 'edit_subject_{}'.format(sub_id)
    }
    return response

@subject.route('/<sub_id>', methods=['DELETE'])
def delete_subject(sub_id):
    response = {
        'results': 'delete_subject_{}'.format(sub_id)
    }
    return response

@subject.route('/<sub_id>/questions', methods=['GET'])
def get_questions(sub_id):
    response = {
        'results': 'get_subject{}_questions'.format(sub_id)
    }
    return response

