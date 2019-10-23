from passlib.hash import sha256_crypt

from db_handler import firebase_handler as fb_handle

def verify(db_url, username, password_candidate):
    db_handler = fb_handle.FirebaseEntryPoint.create()
    if is_username(db_handler, db_url, username):
        user_data = db_handler.retrieve_data(db_url, username)
        password = db_handler.retrieve_password_from_fb_data(user_data)
        if is_password_correct(password_candidate, password):
            return (True, None)
        else:
            return (False, 'Password Incorrect')
    return (False, 'Username Incorrect')

def is_username(db_handler, db_url, username):
    data = db_handler.retrieve_data(db_url, username)
    return data != None

def is_password_correct(password_candidate, password):
    return sha256_crypt.verify(password_candidate, password)
