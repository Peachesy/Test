
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep, strftime, localtime, time



url = "https://www.baidu.com"

s = Service(executable_path=r'/Users/daisy/BrowserDrivers/chromedriver')
driver = webdriver.Chrome(service=s)

# 定义页面元素
img_search = "soutu-btn"  # by class name
choose_img = "upload-pic"  # by class name
search = "soutu-url-btn soutu-url-btn-new"

driver.get(url)
# driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,img_search).click()
driver.find_element(By.CLASS_NAME,choose_img).send_keys("/Users/daisy/PycharmProjects/Test/PccwGlobal/part1/cat.png")
sleep(5)
file_name = strftime("%Y%m%d-%H%M%S", localtime(time()))
driver.save_screenshot("file_name.png")

driver.quit()