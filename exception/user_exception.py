class UserInfoException(Exception):
    ...

class UserNotFoundError(UserInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "User not found."

class UserAlreadyExists(UserInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "User already exists."
