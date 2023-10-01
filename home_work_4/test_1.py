import time
import yaml
from testpage import OperationsHelper
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', "test_login_negative FAIlED"


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pswd"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAIlED"


def test_add_post(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    #testpage.go_to_site()
    #testpage.enter_login(testdata["login"])
    #testpage.enter_pass(testdata["pswd"])
    #testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata["title"])
    testpage.add_description(testdata["description"])
    testpage.add_content(testdata["content"])
    testpage.click_save_post_button()
    time.sleep(2)
    assert testpage.find_new_post_title() == f"{testdata['title']}", "test 'add post' FAILED"

def test_add_contact_us(browser):
    logging.info("Test add_contact Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["pswd"])
    # testpage.click_login_button()
    time.sleep(1)
    testpage.click_contact_button()
    time.sleep(1)
    testpage.your_name(testdata["name"])
    testpage.your_email(testdata["email"])
    testpage.your_content(testdata["contact_content"])
    testpage.click_save_contact_button()
    time.sleep(2)
    assert testpage.get_alert() == "Form successfully submitted", "test 'contact us' FAILED"


