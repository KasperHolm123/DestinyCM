from django.shortcuts import render

#region views
def index(response):
    return render(response, 'main/base.html', {})

def login(response):
    return render(response, 'main/authentication/login.html', {})

def overview(response):
    return render(response, 'main/home/overview.html', {
        'request_response': test_function(response)
    })
#endregion

#region view related functions
from .api_handling import endpoints
client = endpoints.EndpointClient()
def test_function(request):
    #variables
    request_response = None
    character_id = None
    membershipType, destinyMembershipId = 3, 4611686018467683056
        
    if request.method == 'POST':
        if 'endpoint_btn' in request.POST:
            #GET or POST endpoint
            try:
                #GET account membership details
                request_response = client.get_endpoint(\
                    f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200')
                character_id = request_response['Response']['characters']['data']
            except endpoints.ApiError as e:
                print(f'breh: {str(e)}')
            print(character_id)
    
    return character_id

#endregion