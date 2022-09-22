from .core import Core

core = Core()

class EndpointClient:
    
    def get_endpoint(self, endpoint: str):
        response = core.session.get(url=endpoint, headers=core.HEADERS)
        if response.reason != 'OK':
            print(f"Authorization failed: {response.status_code}\n")
            raise AuthTokenError()
        return response.json()
        
    def get_account_type_id(self):
        '''
        Use this function to get relevant user details.\n

        :returns: membershipType, membershipId
        '''

        user_details_endpoint = 'https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/'
        response = core.session.get(url=user_details_endpoint, headers=core.HEADERS)
        if response.reason != 'OK':
            self.authenticate_user()
            response = response
        
        return response.json()['Response']['destinyMemberships'][0]['membershipType'], \
            response.json()['Response']['destinyMemberships'][0]['membershipId']

    def authenticate_user(self):
        '''
        Authenticates a user.\n
        Returns:\n
        OAuth 2.0 token.
        '''
        
        auth_link = core.session.authorization_url(core.base_auth_url)
        #auth returns a code used in retrieving auth token
        return auth_link[0]

    def get_token(self, redirect_response):
        #returns an auth token
        token_dict = core.session.fetch_token(
            include_client_id=True,
            client_id=core.client_id,
            token_url=core.token_url,
            authorization_response=redirect_response,
        )
        
        #save token to local storage
        open('website/static/python_logic/local_data/token.txt', 'w').write(token_dict['access_token'])

        return token_dict['access_token']

class AuthTokenError(Exception):
    def __init__(self, message='Token invalid. Re-authenticate'):
        self.message = message
        super().__init__(self.message)
        

if __name__ == '__main__': # testing purposes
    client = EndpointClient()
    client.get_endpoint('')