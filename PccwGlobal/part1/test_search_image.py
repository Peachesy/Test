import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep, strftime, localtime, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
search by an image in www.baidu.com
I would like to perform a ‘Search by Image’ and visit the result specified on a configuration file
(i.e. VISIT_RESULT=“3” to visit the third result).
Use Selenium Webdriver or any alternative framework to complete this exercise.
Requisites
	- Must store an screen shot of the last visited page
	- Should validate that the search results are related to the used image
"""


class TestSearchImg:

    url = "https://www.baidu.com"

    s = Service(executable_path=r'/Users/daisy/BrowserDrivers/chromedriver')
    driver = webdriver.Chrome(service=s)

    # 定义页面元素
    img_search = "soutu-btn"  # by class name
    choose_img = "upload-pic"  # by class name
    search = "soutu-url-btn soutu-url-btn-new"
    result_div = '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div/a'  # by xpath
    title = '//*[@id="ssr-content"]//div[starts-with(@class,"app-module")][2]//div[contains(@class,"index-module")]//div[contains(@class,"index-module")][1]'   # xpath  '//*[@id="ssr-content"]/div[2]/div/div[1]/div/div/div[1]'
    guide = "graph-guide-info-btn"  # class name

    title_text = ''

    def setup(self):
        self.driver.get(self.url)
        self.driver.fullscreen_window()

    def teardown(self):
        self.driver.quit()

    def search_img(self):
        self.driver.find_element(By.CLASS_NAME,self.img_search).click()
        self.driver.find_element(By.CLASS_NAME,self.choose_img).send_keys("/Users/daisy/PycharmProjects/Test/PccwGlobal/part1/cat.png")
        sleep(5)
        # 获取当前窗口的句柄
        origin_handle = self.driver.current_window_handle
        # print("origin_handle",origin_handle)
        file_name = "search-" + strftime("%Y%m%d-%H%M%S", localtime(time())) + ".png"
        self.driver.save_screenshot(file_name)

        # 处理引导弹窗
        try:
            ele = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.XPATH, self.result_div))
        except TimeoutException:
            if self.driver.find_element(By.CLASS_NAME,self.guide):
                self.driver.find_element(By.CLASS_NAME, self.guide).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        self.driver.execute_script("arguments[0].click();", ele)
        sleep(5)
        # 跳到新窗口，获取所有句柄
        handles = self.driver.window_handles
        # print("All handles:", handles)
        for i in handles:
            if i != origin_handle:
                self.driver.switch_to.window(i)
        self.title_text = self.driver.find_element(By.XPATH,self.title).get_attribute('innerText')

        # 截图
        res_file_name = "result-" + strftime("%Y%m%d-%H%M%S", localtime(time())) + ".png"
        self.driver.save_screenshot(res_file_name)

    def test_search_img(self):
        self.search_img()
        assert '猫' in str(self.title_text)


if __name__ == '__main__':
    pytest.main()