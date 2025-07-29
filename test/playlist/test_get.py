import requests
from config import BASE_URI
from src.assertions.status_code import assert_status_code_200

def test_get_playlist(get_token):
    url = f"{BASE_URI}/v1/playlists/2trIWXYIZ6NZt7Ydp1NKSN"
    token = get_token
    print(token)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token
    } 
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)


def test_get_categories(get_token):
    url = f"{BASE_URI}/v1/browse/categories"
    token = get_token
    print(token)
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)


def test_get_playlist1(get_token):
    url = f"{BASE_URI}/v1/playlists/2trIWXYIZ6NZt7Ydp1NKSN"
    token = get_token
    print(token)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token
    } 
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)


def test_get_categories1(get_token):
    url = f"{BASE_URI}/v1/browse/categories"
    token = get_token
    print(token)
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)
    
def test_get_playlist2(get_token):
    url = f"{BASE_URI}/v1/playlists/2trIWXYIZ6NZt7Ydp1NKSN"
    token = get_token
    print(token)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token
    } 
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)


def test_get_categories2(get_token):
    url = f"{BASE_URI}/v1/browse/categories"
    token = get_token
    print(token)
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)

def test_get_playlist3(get_token):
    url = f"{BASE_URI}/v1/playlists/2trIWXYIZ6NZt7Ydp1NKSN"
    token = get_token
    print(token)
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token
    } 
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)


def test_get_categories3(get_token):
    url = f"{BASE_URI}/v1/browse/categories"
    token = get_token
    print(token)
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert_status_code_200(response)