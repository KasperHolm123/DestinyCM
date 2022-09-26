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

#urls/redirects
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://bungie.net"
token_endpoint = "https://www.bungie.net/platform/app/oauth/token/"

#session
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

class ApiEndpointCaller:

    # def __init__(self):
    #     self.api_key = api_key
    #     self.client_id = client_id
    #     self.auth_token = auth_token
    #     self.HEADERS = HEADERS
    #     self.session = session
    
    @staticmethod
    def get_endpoint(HEADERS: dict, endpoint: str, component_type: EndpointComponentTypes):
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


class AccountCaller:
    '''
    This class is used to request data concerning
    the end-user's account.
    '''
    
    # def __init__(self):
    #     self.session = session
    #     self.base_auth_url = base_auth_url
    #     self.client_id = client_id
    #     self.token_endpoint = token_endpoint
    
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
    
    @staticmethod  
    def get_account_type_id(HEADERS: dict):
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
        

class BungieError(Exception):
    def __init__(self, reason='Unknown error', status_code='Unknown error'):
        self.reason = reason
        self.status_code = status_code
        super().__init__(self.reason, self.status_code)


# if __name__ == '__main__': # testing purposes
#     pass