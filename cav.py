import requests
import os
import json

def getToken():
    url="https://api.petfinder.com/v2/oauth2/token"
    secrets = os.path.join(os.path.abspath(os.getcwd()), "secrets")
    api_key = None
    secret_key = None
    api_key_file = os.path.join(secrets, "api_key.txt")
    with open(api_key_file, 'r') as f:
        api_key = f.read().strip()
    secret_key_file= os.path.join(secrets, "secret_key.txt")
    with open(secret_key_file, 'r') as f:
        secret_key = f.read().strip()
    data = {'grant_type':'client_credentials', 'client_id':api_key, 'client_secret':secret_key}
    token = json.loads(requests.post(url, data=data, headers='').text)['access_token']
    return token

def getPage():
    token = getToken()
    url = "https://www.petfinder.com/search/dogs-for-adoption/us/nj/07302/?breed%5B0%5D=Cavalier+King+Charles+Spaniel&distance=Anywhere"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=header)
    return response
    






