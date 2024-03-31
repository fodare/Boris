import requests
import os

host_ip = f'{os.environ.get("host_ip")}'
backendapi_port = f'{os.environ.get("backendapi_port", 3001)}'
BACKEND_API_BASE_URL = f"http://{host_ip}:{backendapi_port}"


def get_records():
    response_data = requests.get(f"{BACKEND_API_BASE_URL}/api/v3/Record/records", verify=False)
    if (response_data.status_code == 200):
        recordsList = response_data.json()["data"]
        return recordsList
    return None

def create_record(record_amount, record_type, record_tag, record_note):
    request_body = {
        "amount": float(record_amount),
        "event": f"{record_type}",
        "tag": f"{record_tag}",
        "note": f"{record_note}"
        }
    response_data = requests.post(f"{BACKEND_API_BASE_URL}/api/v3/Record/createRecord", json=request_body, verify=False)
    print(response_data.request.body, response_data.status_code)
    if response_data.status_code == 200:
        return True
    else:
        return False
    
def get_record(id):
    response_data = requests.get(f"{BACKEND_API_BASE_URL}/api/v3/Record/{id}", verify=False)
    if response_data.status_code == 200:
        return response_data.json()["data"]
    return None

def update_record(id, amount, event, tag, note):
    request_body = {
        "amount": float(amount),
        "event": f"{event}",
        "tag": f"{tag}",
        "note": f"{note}"
    }
    respose_data = requests.put(f"{BACKEND_API_BASE_URL}/api/v3/Record/updateRecord/{id}", json=request_body, verify=False)
    if respose_data.status_code == 200:
        return True
    return False

def get_summary(start_date, end_date):
    request_body = {
        "startDate": f"{start_date}",
        "endDate": f"{end_date}"
    }
    response_data = requests.post(f"{BACKEND_API_BASE_URL}/api/v3/Record/byDateRange", json=request_body, verify=False)
    print(response_data.request.body)
    if response_data.status_code == 200:
        return response_data.json()["data"]
    return None