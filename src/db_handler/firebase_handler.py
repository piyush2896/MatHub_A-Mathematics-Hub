import json
import time

import requests
import actors

class FirebaseEntryPoint:
    __instance = None
    FIREBASE_URL = 'https://mathub-ser515.firebaseio.com'

    def __init__(self):
        if FirebaseEntryPoint.__instance != None:
            raise Exception('Cannot re-instantiate a singleton class.')
        FirebaseEntryPoint.__instance = self
        FirebaseEntryPoint.__instance.__initialize_db()

    def __initialize_db(self):
        db_urls = [
            actors.Student.DB_URL,
            actors.Teacher.DB_URL,
            actors.Parent.DB_URL,
            actors.Admin.DB_URL
        ]
        for db_url in db_urls:
            result = requests.get(
                FirebaseEntryPoint.FIREBASE_URL + db_url + '/id.json')
            if result.json() == None:
                requests.post(
                    FirebaseEntryPoint.FIREBASE_URL + db_url + '/id.json',
                    data=json.dumps({'id': actors.START_ID}))

        result = requests.get(
            self.__make_url(actors.Admin.DB_URL, 'admin@mathub.com'))
        if result.json() == None:
            requests.post(
                self.__make_url(actors.Admin.DB_URL, 'admin@mathub.com'),
                data=json.dumps({
                    'username': 'admin@mathub.com',
                    'name': 'Admin',
                    'password': '$5$rounds=535000$7IYKx8vORQNl5hZm$olQ2EqpY51tFq7G9vddkN/FPeNxmd7pBDYCW0//ovj5',
                    'id': 'A100',
                    'login_count': 0
                })
            )

    @staticmethod
    def create():
        if FirebaseEntryPoint.__instance == None:
            FirebaseEntryPoint()
        return FirebaseEntryPoint.__instance

    def __log(self, msg, log_file=None):
        if log_file == None:
            return
        with open(log_file, 'a+') as f:
            f.write(time.strftime('%m-%d-%Y') + '|' +
                    time.strftime('%H:%M:%S') + '\t' + msg +'\n')

    def add_data(self, firebase_url, data, log_file=None):
        try:
            result = requests.post(
                self.__make_url(firebase_url, data['username']),
                data=json.dumps(data))
            self.__log('Data Created: ' + json.dumps(data), log_file)
        except Exception as e:
            self.__log('Exception: ' + str(e), log_file)

    def __make_url(self, firebase_url, username):
        return (FirebaseEntryPoint.FIREBASE_URL + firebase_url + 
                '/{}.json'.format('-'.join(username.split('.'))))

    def update_data(self, firebase_url, data, log_file=None):
        try:
            result = requests.put(self.__make_url(
                firebase_url, data['username']), data=json.dumps(data))
            self.__log('Data Updated: ' + json.dumps(data))
        except Exception as e:
            self.__log('Exception: '+ str(e), log_file)

    def retrieve_data(self, firebase_url, username):
        result = requests.get(self.__make_url(firebase_url, username))
        # Firebase safegaurd. They mock around and change return type
        # Sometimes it is sending a dictionary with its own unique key as key and value
        # as the data. While sometimes it sends the data as dictionary itself.
        result = result.json()
        if result == None or not isinstance(list(result.items())[0][1], dict):
            return result
        return list(result.items())[0][1]

    def retrieve_password_from_fb_data(self, data):
        return data['password']

    def retrieve_last_id(self, firebase_url, log_file=None):
        try:
            result = requests.get(
                FirebaseEntryPoint.FIREBASE_URL + firebase_url + '/id.json')
            self.__log('Data Retrieved: ' + json.dumps(id_dict), log_file)
        except AttributeError as e:
            self.__log('Exception: ' + str(e), log_file)
            return None

        data = result.json()
        if data == None:
            return None
        id_dict = list(data.items())[0][1]
        return id_dict['id']

    def update_id(self, firebase_url, log_file=None):
        try:
            result = requests.get(
                FirebaseEntryPoint.FIREBASE_URL + firebase_url + '/id.json')
            fb_id, id_dict = list(result.json().items())[0]
            self.__log('Data Retrieved: ' + json.dumps(id_dict), log_file)
        except AttributeError as e:
            self.__log('Exception: ' + str(e), log_file)
            raise IdNotFoundError('Id not found at: {}{}'.format(
                FirebaseEntryPoint.FIREBASE_URL, firebase_url))

        last_id = id_dict['id']
        result = requests.put(
            FirebaseEntryPoint.FIREBASE_URL + firebase_url + '/id.json',
            data=json.dumps({fb_id: {'id': last_id+1}}))

        return last_id+1

    def set_id(self, firebase_url, id, log_file=None):
        try:
            requests.put(
                FirebaseEntryPoint.FIREBASE_URL + firebase_url + '/id.json',
                data={'id': id})
            self.__log('Data Added: ' + json.dumps({'id': id}), log_file)
        except:
            self.__log('Exception: ' + str(e), log_file)

    def increment_login_count(self, firebase_url, username):
        data = self.retrieve_data(firebase_url, username)
        data['login_count'] += 1
        requests.put(
            self.__make_url(firebase_url, username),
            data=json.dumps(data))
        
    def retrieve_assignments_for_grade(self, firebase_url, grade):
        assignments = requests.get(
            FirebaseEntryPoint.FIREBASE_URL + firebase_url + '/' + str(grade) + '.json')
        return assignments.json()
