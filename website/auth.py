import webbrowser
from flask import Flask, Blueprint, render_template, request, flash
from .static.python_logic import bungie_api

auth = Blueprint('auth', __name__)
client = bungie_api.Client()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    redirect_url = None
    request_response = None
    if request.method == 'POST':
        #run this code only if the request is sent by an element with name 'request_auth_button'
        if request.form.get('request_auth_button') != None:
            redirect_url = client.authenticate_user()
            webbrowser.open_new_tab(redirect_url)

        if request.form.get('auth_button') != None:
            try:
                client.get_token(request.form.get('redirect_input'))
            except:
                flash('Invalid authorization code.', category='error')

        if request.form.get('login_button') != None:
            request_response = client.get_user_details()

    return render_template('auth/login.html', re_response=request_response, data=redirect_url)