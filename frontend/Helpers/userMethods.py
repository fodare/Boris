import requests

BACKEND_API_BASE_URL = 'http://localhost:3001'


def check_user_credentials(userName, password):
    request_body = {
        "userName": f"{userName}",
        "password": f"{password}"
    }
    response_data = requests.post(
        f"{BACKEND_API_BASE_URL}/api/v2/auth/login", json=request_body)
    if response_data.status_code == 200:
        json_response = response_data.json()
        if json_response['success']:
            return True
        return False
    else:
        return False


def check_user_name(username):
    response_data = requests.get(
        f"{BACKEND_API_BASE_URL}/api/v2/auth/{username}")
    if response_data.status_code == 200:
        json_content = response_data.json
        user_info = json_content['data']
        return user_info
    return null
