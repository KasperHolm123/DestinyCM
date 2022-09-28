import os

from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
from .bungie_manifest.destiny2_definitions import EndpointComponentTypes
from .api_response_parser import ResponseParser


#load environmental variables
load_dotenv(dotenv_path='.env')

#authentication variables
api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
auth_token = None

#urls/redirects
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://bungie.net"
token_endpoint = "https://www.bungie.net/platform/app/oauth/token/"

#session
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

HEADERS = {'X-API-KEY': api_key,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {auth_token}'}
    

def generic_api_call(HEADERS: dict, endpoint: str, component_type: EndpointComponentTypes):
    '''
    GET or POST endpoint.\n
    :raises: ApiError on exceptions.
    '''
    
    url = f'https://www.bungie.net/Platform{endpoint}?components={component_type}'
    response = session.get(url=url, headers=HEADERS)
    
    #.get will always return a message, so it is requred to handle it here.
    if response.reason != 'OK':
        raise BungieError(response.reason, response.status_code)
    return response.json()

def get_characters():
    '''
    Makes an API call to request character data\n
    :returns: character data (map)
    '''
    #variables
    membershipType, destinyMembershipId = get_account_type_id()
    endpoint = f'/Destiny2/{membershipType}/Profile/{destinyMembershipId}'
    component_type = EndpointComponentTypes.CHARACTERS.value
    
    try:
        #GET account membership details
        request_response = generic_api_call(HEADERS, endpoint, component_type)
        return ResponseParser.parse_character_details(request_response)
    except BungieError as e:
        print(e)

def get_account_type_id():
    '''
    Use this function to get relevant user details.\n
    :returns: membershipType, membershipId
    '''

    user_details_endpoint = 'https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/'
    response = session.get(url=user_details_endpoint, headers=HEADERS)
    
    #.get will always return with a message, so it is requred to handle it here.
    if response.reason != 'OK':
        raise BungieError(response.reason)
    
    return ResponseParser.parse_membership_details(response.json())

def build_account(auth_response: str): # TODO: connect a BungieAccount to be used in all api calls.
    auth_token = auth_response
    membership_details = get_account_type_id()
    characters = get_characters()
    
    return BungieAccount(membership_details=membership_details, characters=characters)

class AuthorizationHandler:
    '''
    This class is used to request data concerning
    the end-user's account.
    '''
    
    @staticmethod
    def generate_authentication_link():
        '''
        Generates a link used in user authentication.
        '''
        
        return session.authorization_url(base_auth_url)[0]

    @staticmethod
    def get_token(redirect_response: str = None):
        '''
        Takes a redirect URL argument to fetch an OAuth Token\n
        :returns: OAuth Token
        '''
        
        #returns an auth token
        return session.fetch_token(
            include_client_id=True,
            client_id=client_id,
            token_url=token_endpoint,
            authorization_response=redirect_response,
        )

        
class BungieAccount:
    
    membership_details: dict
    characeters: dict
    
    def __init__(self, membership_details: dict, characters: dict):
        self.membership_details = membership_details
        self.characeters = characters


class BungieError(Exception):
    def __init__(self, reason='Unknown error', status_code='Unknown error'):
        self.reason = reason
        self.status_code = status_code
        super().__init__(self.reason, self.status_code)


# if __name__ == '__main__': # testing purposes
#     pass