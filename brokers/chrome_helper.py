import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from models.login_model import LoginModel


class ChromeHelper:
    """

    """
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=options)

    def login(self, login_model: LoginModel, url: str):
        """

        :param login_model:
        :param url:
        :return:
        """
        self.browser.get(url)

        time.sleep(5)
        username = self.browser.find_element_by_id(login_model.username_element)
        password = self.browser.find_element_by_id(login_model.password_element)

        username.send_keys(login_model.username)
        password.send_keys(login_model.password)
        time.sleep(5)

        self.browser.find_element_by_name("submit").click()

    def get_rows_table(self, name: str) -> list:
        """

        :param name:
        :return:
        """
        return self.browser.find_element_by_id(name).find_elements_by_tag_name("tr")
