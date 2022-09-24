from django.shortcuts import render, redirect
from .forms import AuthenticateAccount

#region views
def index(response):
    return render(response, 'main/base.html', {})

def login(response):
    get_authentication_token(response)
    return render(response, 'main/authentication/login.html', {})

def overview(response):
    return render(response, 'main/home/overview.html', {
        'request_response': get_character_data(response)
    })
#endregion

#region view related functions
from .api_handling import endpoints
client = endpoints.EndpointClient()
def get_character_data(request):
    '''
    Makes an API call to request character data\n
    :returns: character data (map)
    '''
    #variables
    request_response = None
    character_id = None
    membershipType, destinyMembershipId = 3, 4611686018467683056
        
    if request.method == 'POST':
        if 'endpoint_btn' in request.POST:
            try:
                #GET account membership details
                request_response = client.get_endpoint(\
                    f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200')
                character_id = request_response['Response']['characters']['data']
            except endpoints.ApiError as e:
                print(f'breh: {str(e)}')
    
    return character_id

def get_authentication_token(request):
    import webbrowser
    '''
    Authenticate user\n
    :param request: data from view form.
    '''
    redirect_url = None

    if request.method == 'POST':
        return redirect('overview') # doesn't work??

        if 'request_auth_button' in request.POST:
            redirect_url = client.authenticate_user()
            webbrowser.open_new_tab(redirect_url)

        if 'auth_button' in request.POST:
            try:
                request.session['token'] = client.get_token(request.POST['redirect_input'])
                request.session['membershipType'], request.session['destinyMembershipId'] = client.get_account_type_id()
            except Exception as e:
                print(f'Error: {str(e)}')

#endregion