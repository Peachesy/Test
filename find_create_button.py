"""
<button _ngcontent-wnh-c420="" mat-button = "" color = "primary"
type = "button" class="mat-focus-indicator mat-button mat-button-base mat-primary ng-star-inserted">
<span class = "mat-button-wrapper">Clear</span>
<span matripple = "" class="mat-ripple mat-button-ripple"></span>
<span class = "mat-button-focus-overlay"></span>
</button>
"""
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



page_url = "http://localhost:63342/Test/test.html?_ijt=btslhgs6e91sasrbo98u1joo6k&_ij_reload=RELOAD_ON_SAVE"
button = "mat-button-wrapper"
s = Service(executable_path=r'/Users/daisy/BrowserDrivers/chromedriver')
new_ele = '''
var add_scr = document.createElement('script')
add_scr.type = 'text/javascript'
add_scr.text = 'alert("创建成功！")'
document.head.appendChild(add_scr);
'''

driver = webdriver.Chrome(service=s)
driver.get(page_url)
try :
    # 找button
    driver.find_element(by=By.CLASS_NAME, value=button)
    time.sleep(1)
    # 创建一个新元素
    try:
        driver.execute_script(new_ele)
        alert = driver.switch_to.alert
        time.sleep(1)
        text = alert.text
        alert.accept()
        time.sleep(1)
        if text == "创建成功！":
            print("创建新元素成功，即将退出")
            driver.quit()
    except NoAlertPresentException:
        print("新元素创建失败，即将退出")
        driver.quit()

except NoSuchElementException:
    print("没找到button")






