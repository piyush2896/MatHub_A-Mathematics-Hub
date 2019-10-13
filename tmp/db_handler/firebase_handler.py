import json
import time

import requests

class FirebaseEntryPoint:
    __instance = None
    FIREBASE_URL = 'https://mathub-ser515.firebaseio.com'

    def __init__(self):
        if FirebaseEntryPoint.__instance != None:
            raise Exception('Cannot re-instantiate a singleton class.')
        FirebaseEntryPoint.__instance = self

    @staticmethod
    def create():
        if FirebaseEntryPoint.__instance == None:
            FirebaseEntryPoint()
        return FirebaseEntryPoint.__instance

    def add_data(self, firebase_url, data, log_file=None):
        try:
            result = requests.post(self.__make_url(firebase_url, data), data=json.dumps(data))
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

    def __make_url(self, firebase_url, data):
        return (FirebaseEntryPoint.FIREBASE_URL + firebase_url + 
                '/{}.json'.format(data['username'].split('.')[0]))

    def retrieve_data(self, firebase_url, username):
        result = requests.get(FirebaseEntryPoint.FIREBASE_URL + firebase_url +
                              '/{}.json'.format(username.split('.')[0]))
        return result.json()

    def retrieve_password_from_fb_data(self, data):
        data_to_list_of_tuples = list(data.items())
        data_dict = data_to_list_of_tuples[0][1]
        return data_dict['password']