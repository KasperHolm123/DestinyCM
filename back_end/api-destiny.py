import requests
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os
import json

load_dotenv()

#authentication variables
api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')

#urls/redirects
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://bungie.net"
token_url = "https://www.bungie.net/platform/app/oauth/token/"
get_user_details_endpoint = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"

#session
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

auth_link = session.authorization_url(base_auth_url)
print(f"Auth link: {auth_link[0]}")

#auth returns a code used in retrieving auth token
redirect_response = input("Insert redirect url incl. params: ")

session.fetch_token(
    include_client_id=True,
    client_id=client_id,
    token_url=token_url,
    authorization_response=redirect_response,
)

#all requests need an api key
additional_headers = {'X-API-KEY': os.getenv('API_KEY')}

response = session.get(url=get_user_details_endpoint, headers=additional_headers)

print(f"RESPONSE STATUS: {response.status_code}")
print(f"RESPONSE REASON: {response.reason}")
print(f"REPONSE TEXT: \n{response.text}")


def main():
    #dictionary to hold headers
    HEADERS = {'X-API-Key': '52f79a4b666d45f2b38a0700d9a0ee29'}

    #request templates
    urlPrefix = 'https://www.bungie.net'
    url = '/Platform/Destiny2/Manifest//'
    membershipType = 254
    destinyMembershipId = 16533207
    displayName = 'TowelieTrip'

    # relevant vendor hashes
    ada1_hash = 350061650

    r = requests.get(f"{urlPrefix}{url}", headers=HEADERS)

    json_object = json.dumps(r.json(), indent=2)

    with open('Local Testing\\data.json', 'w') as f:
        f.write(json_object)

def authorization():
    pass
        
def mainfest_download():
    r = requests.get('https://bungie.net/common/destiny2_content/json/en/DestinyInventoryItemDefinition-c749fcce-2388-496f-b5a6-4859830183e4.json')
    json_object = json.dumps(r.json(), indent=2)
    with open('Local Testing\\manifest.json', 'w') as f:
        f.write(json_object)