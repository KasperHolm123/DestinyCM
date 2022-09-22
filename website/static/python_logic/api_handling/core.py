from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

class Core:
    #load environmental variables
    load_dotenv(dotenv_path='.env')

    #authentication variables
    api_key = os.getenv('API_KEY')
    client_id = os.getenv('CLIENT_ID')
    token_dict = open('website/static/python_logic/local_data/token.txt', 'r').readline()
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