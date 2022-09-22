import webbrowser
from flask import Flask, Blueprint, render_template, request, flash, url_for, redirect, session
from .static.python_logic.api_handling import endpoints

auth = Blueprint('auth', __name__)
client = endpoints.EndpointClient()

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
                session['token'] = client.get_token(request.form.get('redirect_input'))
                session['membershipType'], session['destinyMembershipId'] = client.get_account_type_id()
                flash('Authentication successful', category='success')
                return redirect(url_for('views.overview'))
            except Exception as e:
                flash(str(e), category='error')

    return render_template('auth/login.html', re_response=request_response, data=redirect_url)