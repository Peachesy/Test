import pytest
from selenium import webdriver
import requests
"""
Create a method that would allow 3 different types of logins.
"""


class TestLoginPage:

    username_button = ""
    password_button = ""
    submit_button = ""
    succ_data = [{"username":"Admin",
             "password":"Admin"},
            {"username":"Student",
             "password":"Student"},
            {"username":"Teacher",
             "passowrd":"Teacher"}]
    fail_data = [{"username":"Admin1",
                 "password":"Admin"},
                {"username":"Student2",
                 "password":"Student"},
                {"username":"Teacher3",
                 "passowrd":"Teacher"},
                 {"username":"admin",
                 "passowrd":""},
                 {"username": "",
                  "passowrd": "admin"},
                 {"username": "",
                  "passowrd": ""}]
    white_list = ['Admin','Student','Teacher']
    login_url = ""
    # driver = webdriver.chrome()
    # driver.get(login_url)

    def login(self,username,password):
        if username in self.white_list:
            # self.driver.find_element_by_id(self.username_button).send_keys(username)
            # self.driver.find_element_by_id(self.password_button).send_keys(password)
            # self.driver.find_element_by_id(self.submit_button).click()
            r = requests.request('POST',url=self.login_url,params={username:password})
            if r.status_code == 200:
                print("登录成功")
                return True
        else:
            print("请联系管理员")
            return False


    def setup(self):
        pass

    def teardown(self):
        # self.driver.quit()
        pass

    @pytest.mark.parametrize('param', succ_data)
    def test_login_success(self,param):
        assert self.login(param.get('username'),param.get('password'))

    @pytest.mark.parametrize('param', fail_data)
    def test_login_failed(self, param):
        assert self.login(param.get('username'), param.get('password'))



if __name__ == '__main__':
    pytest.main()








