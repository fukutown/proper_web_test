from flask import Flask, request, jsonify
#from app import create_app
from flask_cors import CORS
import json


app = Flask(__name__)

config = {
  'ORIGINS': [
    'http://localhost:8080',  # Vue
    'http://127.0.0.1:8080',  # Vue
  ]
}
CORS(app, resources={ r'/*': {'origins': config['ORIGINS']}}, supports_credentials=True)
# env = os.getenv('FLASK_CONFIG')
# app = create_app('default')

from app.controllers.settings import subject, user
app.register_blueprint(subject, url_prefix='/api/settings/subjects')
app.register_blueprint(user, url_prefix='/api/settings/users')

@app.route('/api/')
def index():
    return "hello fukui"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
