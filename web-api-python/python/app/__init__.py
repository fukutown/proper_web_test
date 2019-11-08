from flask import current_app, Flask
from config import config
from flask_cors import CORS

"""
app = Flask(__name__)
env_type = 'default'
app.config.from_object(config[env_type])
app.config['JSON_AS_ASCII'] = False
CORS(app)
"""

# 環境変数から設定値を読み込む用
def create_app(app, env_type):
    print('called init.py')
    print(f'{app}')
    app.config.from_object(config[env_type])
    app.config['JSON_AS_ASCII'] = False
    CORS(app)
    from .controllers import sub
    app.register_blueprint(sub, url_prefix='/api/settings')

    return app
