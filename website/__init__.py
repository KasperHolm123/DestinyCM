from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'afoiaefj9823479oijiosgp98q34pahgrjenfdkæzkhg74'

    return app