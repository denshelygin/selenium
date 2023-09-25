import time
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_step_1(x_selector1, x_selector2, x_selector3, btn_selector, error_code):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3).text
    assert err_label == error_code, "test_step_1 failed"


def test_step_2(x_selector1, x_selector2, x_selector4, btn_selector, account_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pswd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    code_label = site.find_element("xpath", x_selector4).text
    assert code_label == account_name, "test_step_2 failed"
    time.sleep(3)

def test_step_3(x_selector1, x_selector2, x_selector5, x_selector6, x_selector7, x_selector8,
                btn_selector, account_name, btn_create, btn_create_item, title_post):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pswd"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    btn = site.find_element("xpath", btn_create)
    btn.click()
    input3 = site.find_element("xpath", x_selector5)
    input3.clear()
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", x_selector6)
    input4.clear()
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", x_selector7)
    input5.clear()
    input5.send_keys(testdata["content"])
    btn = site.find_element("xpath", btn_create_item)
    btn.click()
    time.sleep(3)
    code_label = site.find_element("xpath", x_selector8).text
    assert code_label == title_post, "test_step_3 failed"
