from django.shortcuts import render, redirect

#region views
def index(response):
    return render(response, 'main/base.html', {})

def login(response):
    generate_authentication_link(response)
    if get_authorization_token(response):
        return redirect('main:overview')
    return render(response, 'main/authentication/login.html', {})

def overview(response):
    # I need to somehow pass the auth token to every api call made
    HEADERS['Authorization'] = f'Bearer {response.session["authorization"]["access_token"]}'
    return render(response, 'main/home/overview.html', {
        'request_response': get_character_data(response)
    })
#endregion

#region view related functions
from .bungie_api import api_client
from .bungie_api.api_client import ApiEndpointCaller, AccountCaller, BungieError
from .bungie_api.bungie_manifest.destiny2_definitions import EndpointComponentTypes
from .bungie_api.api_response_parser import ResponseParser

#additional headers required for every request sent to the API
global HEADERS
HEADERS = {'X-API-KEY': api_client.api_key,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': None}

def get_character_data(request):
    '''
    Makes an API call to request character data\n
    :returns: character data (map)
    '''
    #variables
    membershipType, destinyMembershipId = request.session['membershipType'], request.session['destinyMembershipId']
    if request.method == 'POST' and 'endpoint_btn' in request.POST:
        endpoint = f'/Destiny2/{membershipType}/Profile/{destinyMembershipId}'
        component_type = EndpointComponentTypes.CHARACTERS.value
        try:
            #GET account membership details
            request_response = ApiEndpointCaller.get_endpoint(HEADERS, endpoint, component_type)
            return ResponseParser.parse_character_details(request_response)
        except BungieError as e:
            print(e)

def generate_authentication_link(request):
    '''
    Authenticate user\n
    :param request: data from view form.
    '''
    import webbrowser

    if request.method == 'POST' and 'request_auth_button' in request.POST:
        webbrowser.open_new_tab(AccountCaller.generate_authentication_link())

def get_authorization_token(request):
    if request.method == 'POST' and 'auth_button' in request.POST:
        try:
            request.session['authorization'] = AccountCaller.get_token(request.POST["redirect_input"])
            request.session['membershipType'], request.session['destinyMembershipId'] = AccountCaller.get_account_type_id(HEADERS)
            return True # redirect must be used in view function
        except BungieError as e:
            print(e)
#endregion