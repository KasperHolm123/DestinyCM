from flask import Blueprint, render_template, request, flash
from .static.python_logic.api_handling import endpoints

views = Blueprint('views', __name__)
client = endpoints.EndpointClient()

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('views/index.html')

@views.route('/overview', methods=['GET', 'POST'])
def overview():
    request_response = None
    character_id = None
    try:
        membershipType, destinyMembershipId = client.get_account_type_id()
    except Exception as e:
        flash(str(e), category='error')
    if request.method == 'POST':
        if request.form.get('endpoint_btn') != None:
            try:
                request_response = client.get_endpoint(\
                    f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200')
                character_id = request_response['Response']['characters']['data']
            except Exception as e:
                flash(str(e), category='error')
        pass

    return render_template('views/overview.html', request_response=character_id)