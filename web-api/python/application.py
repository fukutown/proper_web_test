from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# 日本語文字化け対策(すぐに消すかも)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/')
def index():
    return "hello fukui"

@app.route('/api/settings/tests', methods=['GET'])
def get_tests():
    return jsonify({'results': 'return test list'})

@app.route('/api/settings/tests', methods=['POST'])
def create_test():
    data = json.loads(request.data.decode('utf-8'))
    name = str(data['name'])
    res = {
        'name': name,
        'func': 'create'
    }
    return jsonify({'results': res})

@app.route('/api/settings/tests/<id>', methods=['POST'])
def edit_test(id):
    data = json.loads(request.data.decode('utf-8'))
    name = str(data['name'])
    res = {
        'id': id,
        'name': name,
        'func': 'edit'
    }
    return jsonify({'results': res})

@app.route('/api/settings/tests/<id>', methods=['DELETE'])
def delete_test(id):
    res = {
        'id': id,
        'func': 'delete'
    }
    return jsonify({'results': res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
