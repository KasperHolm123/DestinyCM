import requests
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os
import json

load_dotenv()

#authentication variables
api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
token_dict = open('token.txt').readline()
redirect_response = None

#urls/redirects
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://bungie.net"
token_url = "https://www.bungie.net/platform/app/oauth/token/"
get_user_details_endpoint = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"

#session
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

#all requests need an api key
additional_headers = {'X-API-KEY': api_key}

def main():
    response = session.get(url=get_user_details_endpoint, headers=additional_headers)
    if response.reason != 'OK':
        print(f"Authorization failed: {response.status_code}\n{response.reason}\n{response.text['Message']}")
        authorization()

    print(f"RESPONSE STATUS: {response.status_code}")
    print(f"RESPONSE REASON: {response.reason}")
    print(f"REPONSE TEXT: \n{response.text}")
    

def authorization():    
    auth_link = session.authorization_url(base_auth_url)
    print(f"Auth link: {auth_link[0]}")

    #auth returns a code used in retrieving auth token
    redirect_response = input("Insert redirect url incl. params: ")
    token_dict = session.fetch_token(
        include_client_id=True,
        client_id=client_id,
        token_url=token_url,
        authorization_response=redirect_response,
    )
    response = session.get(url=get_user_details_endpoint, headers=additional_headers)
    return response

main()




def mainfest_download():
    r = requests.get('https://bungie.net/common/destiny2_content/json/en/DestinyInventoryItemDefinition-c749fcce-2388-496f-b5a6-4859830183e4.json')
    json_object = json.dumps(r.json(), indent=2)
    with open('Local Testing\\manifest.json', 'w') as f:
        f.write(json_object)