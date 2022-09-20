import requests
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os
import json

#load environmental variables
load_dotenv(dotenv_path='.env')

#authentication variables
api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
# token_dict = open('token.txt').readline()
redirect_response = None

#urls/redirects
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://bungie.net"
token_url = "https://www.bungie.net/platform/app/oauth/token/"
get_user_details_endpoint = None

#session
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

#additional headers required for every request sent to the API
'''HEADERS = {'X-API-KEY': api_key,
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': f'Bearer {token_dict}'}'''

def main():
    response = session.get(url=get_user_details_endpoint)#, headers=HEADERS
    if response.reason != 'OK':
        print(f"Authorization failed: {response.status_code}\n{response.reason}")
        response = response

    #write response to terminal and save it to a local file * TEMPORARY *
    print(f"RESPONSE STATUS: {response.status_code}")
    print(f"RESPONSE REASON: {response.reason}")
    print(f"REPONSE TEXT: \n{response.text}")
    open('data.json', 'a').write(response.text)

def get_user_details():
    '''
    Use this function to get relevant user deatails, such as:\n
    Membership ID,\n
    Membership Type,\n
    as well as others.\n

    This data is used in a lot of GET & POST endpoints relevant only to a specific account.
    '''
    user_details_endpoint = 'https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/'
    response = session.get(url=user_details_endpoint)#, headers=HEADERS
    if response.reason != 'OK':
        get_token()
        response = response
    
    #dump json response to a local file * TEMPORARY *
    json_object = json.dumps(response.json(), indent=2)
    open('data.json', 'a').write(json_object)

def get_token():
    '''
    Stores an auth token in a local file, "token.txt"
    '''
    if os.path.isfile('token.txt'):
        current_token = open('token.txt', 'r').readline()
    
    print(f'Auth failed. Click link below to authorize')
    auth_link = session.authorization_url(base_auth_url)
    print(f"Auth link: {auth_link[0]}")

    #auth returns a code used in retrieving auth token
    redirect_response = input("Insert redirect url incl. params: ")

    #returns an auth token
    token_dict = session.fetch_token(
        include_client_id=True,
        client_id=client_id,
        token_url=token_url,
        authorization_response=redirect_response,
    )
    
    #if a new token has been generated, store it locally * TEMPORARY *
    if token_dict['access_token'] != current_token and current_token != None:
        open('token.txt', 'w').write(token_dict['access_token'])

def test_function():
    print(api_key)

if __name__ == '__main__':
    # get_user_details()
    #main()

    with open('data.json') as f:
        data = json.load(f)
    print(data['Response']['destinyMemberships'][0]['membershipType'])
    print(data['Response']['destinyMemberships'][0]['membershipId'])


def mainfest_download():
    r = requests.get('https://bungie.net/common/destiny2_content/json/en/DestinyInventoryItemDefinition-c749fcce-2388-496f-b5a6-4859830183e4.json')
    json_object = json.dumps(r.json(), indent=2)
    with open('Local Testing\\manifest.json', 'w') as f:
        f.write(json_object)