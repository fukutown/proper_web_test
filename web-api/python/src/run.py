from flask import Flask
app = Flask(__name__)

@app.route('/api/')
def index():
    return "hello fukui"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
