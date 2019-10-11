import json
import time

import requests

def add_data(firebase_url, data, log_file=None):
    try:
        result = requests.post(firebase_url, data=json.dumps(data))
        if log_file != None:
            with open(log_file, 'a') as f:
                f.write(time.strftime('%m-%d-%Y') + '|' +
                        time.strftime('%H:%M:%S') +
                        'Data Created: ' + json.dumps(data)+'\n')
    except Exception as e:
        if log_file != None:
            with open(log_file, 'a') as f:
                f.write(time.strftime('%m-%d-%Y') + '|' +
                        time.strftime('%H:%M:%S') +
                        'Exception:' + str(e) + '\n')

def retrieve_data(firebase_url, username):
    result = requests.get(firebase_url + '/{}.json'.format(username.split('.')[0]))
    return result.json()
