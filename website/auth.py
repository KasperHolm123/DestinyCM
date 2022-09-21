from flask import Flask, Blueprint, render_template
from .static.python_logic import bungie_api

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    client = bungie_api.Client()
    data = client.authenticate_user()
    
    return render_template('auth/login.html', data=data)