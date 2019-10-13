from flask import Flask, request, jsonify
#from app import create_app
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
# env = os.getenv('FLASK_CONFIG')
# app = create_app('default')

from app.controllers.settings import subject, user
app.register_blueprint(subject, url_prefix='/api/settings/subjects')
app.register_blueprint(user, url_prefix='/api/settings/users')

@app.route('/api/')
def index():
    return "hello fukui"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
