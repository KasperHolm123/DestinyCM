from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

class EndpointClient:
    #load environmental variables
    load_dotenv(dotenv_path='.env')

    #authentication variables
    api_key = os.getenv('API_KEY')
    client_id = os.getenv('CLIENT_ID', '41471')
    token_dict = None
    redirect_response = None

    #urls/redirects
    base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
    redirect_url = "https://bungie.net"
    token_url = "https://www.bungie.net/platform/app/oauth/token/"
    get_user_details_endpoint = None

    #session
    session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

    #additional headers required for every request sent to the API
    HEADERS = {'X-API-KEY': api_key,
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Authorization': f'Bearer {token_dict}'}


    def __init__(self, auth_token = None):
        self.token_dict = auth_token
        self.HEADERS['Authorization'] = self.token_dict
    
    def get_endpoint(self, endpoint: str):
        '''
        GET or POST endpoint.\n
        :raises: ApiError on exceptions.
        '''
        response = self.session.get(url=endpoint, headers=self.HEADERS)
        #.get will always return a message, so it is requred to handle it here.
        if response.reason != 'OK':
            raise ApiError(response.reason, response.status_code)
        return response.json()
        
    def get_account_type_id(self):
        '''
        Use this function to get relevant user details.\n
        :returns: membershipType, membershipId
        '''

        user_details_endpoint = 'https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/'
        response = self.session.get(url=user_details_endpoint, headers=self.HEADERS)
        #.get will always return with a message, so it is requred to handle it here.
        if response.reason != 'OK':
            raise ApiError(response.reason)
        
        return response.json()['Response']['destinyMemberships'][0]['membershipType'], \
            response.json()['Response']['destinyMemberships'][0]['membershipId']

    def authenticate_user(self):
        '''
        Authenticates a user.\n
        Returns:\n
        OAuth 2.0 token.
        '''
        
        auth_link = self.session.authorization_url(self.base_auth_url)
        #auth returns a code used in retrieving auth token
        return auth_link[0]

    def get_token(self, redirect_response: str = None):
        '''
        Takes a redirect URL argument to fetch an OAuth Token\n
        :returns: OAuth Token
        '''
        #returns an auth token
        token_dict = self.session.fetch_token(
            include_client_id=True,
            client_id=self.client_id,
            token_url=self.token_url,
            authorization_response=redirect_response,
        )

        #save token to local storage
        # open('website/static/python_logic/local_data/token.txt', 'w').write(token_dict['access_token'])
        return token_dict['access_token']

class ApiError(Exception):
    def __init__(self, reason='Unknown error', status_code='Unknown error'):
        self.reason = reason
        self.status_code = status_code
        super().__init__(self.reason, self.status_code)
        

if __name__ == '__main__': # testing purposes
    client = EndpointClient()
    client.authenticate_user()