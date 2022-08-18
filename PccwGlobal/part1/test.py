import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep, strftime, localtime, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.baidu.com"

s = Service(executable_path=r'/Users/daisy/BrowserDrivers/chromedriver')
driver = webdriver.Chrome(service=s)

# 定义页面元素
img_search = "soutu-btn"  # by class name
choose_img = "upload-pic"  # by class name
search = "soutu-url-btn soutu-url-btn-new"
result_div = '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div/a'  # by xpath
title = '/html/head/title'   # xpath
guide = "graph-guide-info-btn"  # class name

driver.get(url)
driver.fullscreen_window()
# driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,img_search).click()
driver.find_element(By.CLASS_NAME,choose_img).send_keys("/Users/daisy/PycharmProjects/Test/PccwGlobal/part1/cat.png")
sleep(5)
file_name = strftime("%Y%m%d-%H%M%S", localtime(time())) + ".png"
driver.save_screenshot(file_name)
# click the third result
# ele = driver.find_element(By.XPATH,result_div)
# 处理引导弹窗
try:
    ele = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.XPATH, result_div))
except TimeoutException:
    driver.find_element(By.CLASS_NAME,guide).click()
driver.execute_script("arguments[0].scrollIntoView();", ele)
driver.execute_script("arguments[0].click();", ele)
# ele.click()
sleep(5)
title_text = driver.find_element(By.XPATH,title).text
print(title_text)
# assert "猫" in title_text


driver.quit()