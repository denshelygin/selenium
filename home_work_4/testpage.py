import time

import requests
import yaml
from selenium.webdriver.common.by import By
from BaseApp import BasePage
import logging

ids = dict()
with open("locators.yaml") as f:
    locators = yaml.safe_load(f)
for locator in locators["xpath"].keys():
    ids[locator] = (By.XPATH, locators["xpath"][locator])
for locator in locators["css"].keys():
    ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def add_title(self, word):
        time.sleep(1)
        self.enter_text_into_field(ids["LOCATOR_TITLE_POST"], word, description="title form")

    def add_description(self, word):
        self.enter_text_into_field(ids["LOCATOR_DESCRIPTION_POST"], word, description="description form")

    def add_content(self, word):
        self.enter_text_into_field(ids["LOCATOR_CONTENT_POST"], word, description="content form")

    def your_name(self, word):
        self.enter_text_into_field(ids["LOCATOR_YOUR_NAME"], word, description="name form")

    def your_email(self, word):
        self.enter_text_into_field(ids["LOCATOR_YOUR_EMAIL"], word, description="email form")

    def your_content(self, word):
        self.enter_text_into_field(ids["LOCATOR_YOUR_CONTENT"], word, description="contact content form")

    # CLICK
    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_save_contact_button(self):
        self.click_button(ids["LOCATOR_CONTACT_US_BTN"], description="safe contact")

    def click_contact_button(self):
        self.click_button(ids["LOCATOR_CONTACT_BTN"], description="contact")

    def click_save_post_button(self):
        self.click_button(ids["LOCATOR_SAVE_POST"], description="save post")

    def click_add_post_button(self):
        self.click_button(ids["LOCATOR_ADD_POST"], description="add post")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(ids["LOCATOR_ERROR_FIELD"], description="error text")

    def login_success(self):
        return self.get_text_from_element(ids["LOCATOR_SUCCESS"], description="positive login")

    def find_new_post_title(self):
        return self.get_text_from_element(ids["LOCATOR_FIND_NEW_POST"], description="find new post")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text


    # TEST API

    def user_login():
        S = requests.Session()
        result = S.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
        response_json = result.json()
        token = response_json.get('token')
        return token


