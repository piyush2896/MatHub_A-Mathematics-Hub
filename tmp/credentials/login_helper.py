from passlib.hash import sha256_crypt

from db_handler import firebase_handler as fb_handle

def verify(db_url, username, password):
    # TODO: Find Username in DB
    # TODO: Check if Password Matches
    return True 

def is_username(db_url, username):
    data = fb_handle.retrieve_data(db_url, username)
    return data != None

def is_password_correct(password_candidate, password):
    return sha256_crypt.verify(password_candidate, password)