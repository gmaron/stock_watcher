""" BullMarkets """
import time

from models.login_model import LoginModel
from utils.config_helper import ConfigHelper
from .chrome_helper import ChromeHelper


class BullMarkets(ChromeHelper):

    def __init__(self):
        super().__init__()
        self.config = ConfigHelper()
        self.model = self.config.get_broker_config(type(self).__name__.upper())
        self.main_words = ["acciones", "fondos", "cedears", "bonos", "total var. $"]


    def login(self, login_model: LoginModel, url: str):
        """

        :param login_model:
        :param url:
        :return:
        """

        config = self.config.get_all_config("BULLMARKETS")

        self.browser.get(url)
        self.browser.execute_script(config["script_modal"])

        time.sleep(5)
        username = self.browser.find_element_by_id(login_model.username_element)
        password = self.browser.find_element_by_id(login_model.password_element)

        username.send_keys(login_model.username)
        password.send_keys(login_model.password)
        time.sleep(5)
        self.browser.execute_script(config["script_login"])

    def get_data(self):
        """

        :return:
        """
        self.login(self.model, "https://bullmarketbrokers.com/")
        time.sleep(10)
        rows = self.get_rows_table("tbody_accountBrief")
        response = {}
        main_words_word = ''
        for row in rows:
            tds: list = list(filter(None, [x.text for x in row.find_elements_by_tag_name("td")]))
            if self.main_words.count(tds[0].lower()) > 0:
                main_words_word = tds[0]
                response[main_words_word] = {}
                response["total"] = tds[1:len(tds)]
                continue
            response[main_words_word][tds[0]] = []
            for i in range(1, len(tds)):
                response[main_words_word][tds[0]].append(tds[i])
        return response
