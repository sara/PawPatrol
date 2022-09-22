import requests
import os

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
    token = requests.post(url, data=data, headers='')
    return token

getToken()
    
    






