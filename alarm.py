import time
import requests
import psutil

url = 'http://localhost:8080'


def send_alarm(url_request, data):
    response = requests.post(url_request, data=data)
    if response.status_code == 200:
        return True
    return False


def run_scrypt():
    while True:
        value = psutil.virtual_memory()
        if value.used > 10000:
            data_dict = {'value.used': int(value.used / 1000000)}
            if send_alarm(url, data=data_dict):
                print('create_records_in_database')
        time.sleep(2)


run_scrypt()
