from django.shortcuts import render, redirect
from ..bungie_api.api_client import BungieError, AuthorizationHandler


def login(response):
    generate_authentication_link(response)
    if get_authorization_token(response):
        return redirect('main:overview')
    return render(response, 'main/authentication/login.html', {})


def get_character_data(request):
    pass

def generate_authentication_link(request):
    '''
    Authenticate user\n
    :param request: data from view form.
    '''
    import webbrowser

    if request.method == 'POST' and 'request_auth_button' in request.POST:
        webbrowser.open_new_tab(AuthorizationHandler.generate_authentication_link())

def get_authorization_token(request):
    if request.method == 'POST' and 'auth_button' in request.POST:
        try:
            request.session['authorization'] = AuthorizationHandler.get_token(request.POST["redirect_input"])
            return True # redirect must be used in view function
        except BungieError as e:
            print(e)