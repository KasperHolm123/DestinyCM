from django.shortcuts import render, redirect
from ..bungie_api import api_client



def overview(response):
    # Setup current logged-in account
    # current_account = api_client.build_account(response.session['authorization']['access_token'])
    return render(response, 'main/home/overview.html', {
        'request_response': get_characters_api(response)
    })
    

def get_characters_api(response):
    if response.method == 'POST' and 'endpoint_btn' in response.POST:
        return api_client.get_characters()