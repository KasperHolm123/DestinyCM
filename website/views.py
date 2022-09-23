from threading import local
from flask import Blueprint, render_template, request, flash, session
import json
from .static.python_logic.api_handling import endpoints

views = Blueprint('views', __name__)
client = endpoints.EndpointClient()

 #region Views/Pages
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('views/index.html')

@views.route('/overview', methods=['GET', 'POST'])
def overview():
    #variables
    request_response = None
    character_id = None

    #try getting current authorized account's membership details
    try:
        membershipType, destinyMembershipId = session['membershipType'], session['destinyMembershipId']
        # auth_token = session['token']
    except:
        flash('No account has been specified. Please login to continue', category='error')

    if request.method == 'POST':
        #GET or POST endpoint
        if request.form.get('endpoint_btn') != None:
            try:
                #GET account membership details
                request_response = client.get_endpoint(\
                    f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200')
                character_id = request_response['Response']['characters']['data']
                flash('Success', category='success')
            except endpoints.ApiError as e:
                flash(str(e), category='error')
        pass

    return render_template('views/overview.html', request_response=character_id)
#endregion

#region data reroutes
@views.route('/fetcheddata', methods=['GET', 'POST']) #this is used as an arbitrary route to collect data
def fetch_data():
    global client

    local_storage = json.loads(request.get_json())
    # print(local_storage) # Printing the new dictionary
    # print(type(local_storage))#this shows the json converted as a python dictionary
    client = endpoints.EndpointClient(local_storage['auth_token'])
    
    return local_storage

#endregion