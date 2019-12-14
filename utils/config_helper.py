import configparser
import os

from models.login_model import LoginModel


class ConfigHelper:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config.read(self.path + '/configs.ini')

    def get_broker_config(self, broker) -> LoginModel:
        data = self.get_all_config(broker=broker)
        return LoginModel(data["username"],
                          data["password"],
                          data["username_element"],
                          data["password_element"])

    def get_all_config(self, broker):
        return self.config[broker]