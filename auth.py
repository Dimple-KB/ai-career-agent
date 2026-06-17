from database import add_user, validate_user


def signup(username, password):
    return add_user(username, password)


def login(username, password):
    return validate_user(username, password)
