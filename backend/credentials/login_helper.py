from passlib.hash import sha256_crypt

def verify(db_instance, username, password):
    # TODO: Find Username in DB
    # TODO: Check if Password Matches
    return True

def is_username(db_instance, username):
    # TODO: Find is username present and return bool
    return True 

def is_password_correct(password_candidate, password):
    return sha256_crypt.verify(password_candidate, password)