import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""

@pytest.fixture()
def btn_selector():
    return "button"

@pytest.fixture()
def error_code():
    return "401"

@pytest.fixture()
def account_name():
    return f"Hello, {testdata['login']}"

@pytest.fixture()
def btn_create():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def x_selector5():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def x_selector6():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def x_selector7():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def btn_create_item():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def x_selector8():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def title_post():
    return testdata['title']

