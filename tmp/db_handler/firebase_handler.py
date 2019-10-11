import json
import time

import requests

def add_data(firebase_url, data, log_file=None):
    result = requests.post(firebase_url, data=json.dumps(data))
    if log_file != None:
        with open(log_file, 'a') as f:
            f.write(time.strftime('%m-%d-%Y') + '|' +
                    time.strftime('%H:%M:%S') +
                    'Data Created: ' + json.dumps(data)+'\n')
