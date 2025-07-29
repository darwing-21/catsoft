import pytest
import requests
from config import Client_Id, Client_Secret, url_token

@pytest.fixture(scope="session")
def get_token():
    url = url_token
    payload = (
        f'grant_type=client_credentials'
        f'&client_id={Client_Id}'
        f'&client_secret={Client_Secret}'
    )
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    response_json = response.json()
    access_token = response_json['access_token']
    return access_token
