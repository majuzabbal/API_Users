from flask import Flask
from flask_mongoengine import MongoEngine

from Routes.User.users_route import users_blueprint

db = MongoEngine()
app = Flask('api_da_maju')

app.config['MONGODB_SETTINGS'] = {
    'db': 'cadastro_usuario',
    'host': 'localhost',
    'port': 27017
}

db.init_app(app)

app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
