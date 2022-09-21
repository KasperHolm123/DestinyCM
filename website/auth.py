from flask import Flask, Blueprint, render_template, request, redirect
from .static.python_logic import bungie_api

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    redirect_url = None
    if request.method == 'POST':
        if request.form.get('auth_button') != None:
            client = bungie_api.Client()
            redirect_url = client.authenticate_user()
            return redirect(redirect_url, code=302)

    return render_template('auth/login.html', data=redirect_url)