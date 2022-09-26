from threading import local
from django.shortcuts import render, redirect

#region views
def index(response):
    return render(response, 'main/base.html', {})

def login(response):
    if get_authentication_token(response):
        return redirect('main:overview')
    return render(response, 'main/authentication/login.html', {})

def overview(response):
    return render(response, 'main/home/overview.html', {
        'request_response': get_character_data(response)
    })
#endregion

#region view related functions
from .bungie_api import destiny2_api
from .bungie_api.bungie_manifest.destiny2_definitions import EndpointComponentTypes
client = destiny2_api.EndpointClient()

def get_character_data(request):
    '''
    Makes an API call to request character data\n
    :returns: character data (map)
    '''
    #variables
    membershipType, destinyMembershipId = request.session['membershipType'], request.session['destinyMembershipId']
    if request.method == 'POST' and 'endpoint_btn' in request.POST:
        endpoint = f'/Destiny2/{membershipType}/Profile/{destinyMembershipId}'
        component_type = EndpointComponentTypes.CHARACTERS
        try:
            #GET account membership details
            request_response = client.get_endpoint(endpoint, component_type)
            return request_response['Response']['characters']['data']
        except destiny2_api.ApiError as e:
            print(e)

def get_authentication_token(request):
    '''
    Authenticate user\n
    :param request: data from view form.
    '''
    import webbrowser

    if request.method == 'POST':
        if 'request_auth_button' in request.POST:
            redirect_url = client.authenticate_user()
            webbrowser.open_new_tab(redirect_url)

        if 'auth_button' in request.POST:
            try:
                request.session['access_token'] = client.get_token(request.POST['redirect_input'])
                request.session['membershipType'], request.session['destinyMembershipId'] = client.get_account_type_id()
                return True # redirect must be used in view function
            except destiny2_api.ApiError as e:
                print(e)
#endregion