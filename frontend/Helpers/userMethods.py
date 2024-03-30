import requests
import os

host_ip = f'{os.environ.get("host_ip")}'
backendapi_port = f'{os.environ.get("backendapi_port")}'
BACKEND_API_BASE_URL = f"http://{host_ip}:{backendapi_port}"


def check_user_credentials(userName, password):
    request_body = {
        "userName": f"{userName}",
        "password": f"{password}"
    }
    response_data = requests.post(
        f"{BACKEND_API_BASE_URL}/api/v3/User/verify", verify=False, json=request_body)
    if response_data.status_code == 200:
        json_response = response_data.json()
        if json_response['success']:
            return True
        return False
    else:
        return False


def check_user_name(username):
    response_data = requests.get(
        f"{BACKEND_API_BASE_URL}/api/v3/User/{username}", verify=False)
    if response_data.status_code == 200:
        json_content = response_data.json()
        user_info = json_content['data']
        return user_info


def get_user_by_id(user_id):
    response_data = requests.get(
        f"{BACKEND_API_BASE_URL}/api/v3/User/userid/{user_id}", verify=False)
    if response_data.status_code == 200:
        json_content = response_data.json()
        user_data = json_content['data']
        return user_data
