import json


class LoginModel:

    def __init__(self, username, password, username_element, password_element):
        self.username = username
        self.password = password
        self.username_element = username_element
        self.password_element = password_element

    @property
    def to_json(self):
        return json.dump({"username": self.username,
                          "password": self.password})
