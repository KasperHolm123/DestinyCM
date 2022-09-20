from flask import Flask, Blueprint, render_template
from .static.python_logic import bungie_api

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = '234879'
    return render_template('auth/login.html', data=data)