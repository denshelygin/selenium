import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
with open('config.yaml', encoding='utf-8') as g:
    data = yaml.safe_load(g)
S = requests.Session()


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def user_login():
    result = S.post(url=data['url'], data={'username': data['login'], 'password': data['pswd']})
    response_json = result.json()
    token = response_json.get('token')
    return token


@pytest.fixture()
def get_description():
    return 'New_description_for_test_HW'


@pytest.fixture()
def post_title():
    return 'TestTitle'
