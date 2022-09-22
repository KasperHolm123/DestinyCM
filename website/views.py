from flask import Blueprint, render_template, request, flash
from .static.python_logic import bungie_api

views = Blueprint('views', __name__)
client = bungie_api.Client()

@views.route('/', methods=['GET', 'POST'])
def home():
    data = request.form #returns whatever gets posted
    if request.method == 'POST':
        pass
    else:
        pass
    return render_template('views/index.html')

@views.route('/overview', methods=['GET', 'POST'])
def overview():
    request_response = None
    if request.method == 'POST':
        if request.form.get('endpoint_btn') != None:
            try:
                membershipType, destinyMembershipId = client.get_account_type_id()
                request_response = client.get_endpoint(f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200')
            except:
                flash('Token invalid', category='error')
        pass

    return render_template('views/overview.html', request_response=request_response)