from django.shortcuts import render, redirect
from .forms import AuthenticateAccount

#region views
def index(response):
    return render(response, 'main/base.html', {})

def login(response):
    if get_authentication_token(response):
        return redirect('main:overview')
    return render(response, 'main/authentication/login.html', {})

def overview(response):
    # print(f'cookies:\n{response.COOKIES}')
    return render(response, 'main/home/overview.html', {
        'request_response': get_character_data(response)
    })
#endregion

#region view related functions
from .bungie_api import destiny2_api
client = destiny2_api.EndpointClient()
def get_character_data(request):
    '''
    Makes an API call to request character data\n
    :returns: character data (map)
    '''
    #variables
    character_id = None
    membershipType, destinyMembershipId = request.session['membershipType'], request.session['destinyMembershipId']
        
    if request.method == 'POST':
        if 'endpoint_btn' in request.POST:
            try:
                #GET account membership details
                request_response = client.get_endpoint(\
                    f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200')
                character_id = request_response['Response']['characters']['data']
            except destiny2_api.ApiError as e:
                print(f'breh: {str(e)}')
    
    return character_id

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
                request.session['token'] = client.get_token(request.POST['redirect_input'])
                request.session['membershipType'], request.session['destinyMembershipId'] = client.get_account_type_id()
                return True # redirect must be used in view function
            except Exception as e:
                print(f'Error: {str(e)}')
#endregion