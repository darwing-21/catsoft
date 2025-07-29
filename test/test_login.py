import requests
from config import Client_Id, Client_Secret, url_token
from src.assertions.status_code import assert_status_code_200, assert_status_code_400
from src.assertions.assertion_general import assert_response_no_empty

def test_login():
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
    assert_status_code_200(response)
    assert_response_no_empty(response)


def test_login_invalid():
    url = url_token
    payload = (
        f'grant_type=client_credentials'
        f'&client_id=4546546521asad4545ads'
        f'&client_secret={Client_Secret}'
    )
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert_status_code_400(response)    
    assert_response_no_empty(response)