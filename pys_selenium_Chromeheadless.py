from bs4 import BeautifulSoup
from bs4 import re
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time, os
import goferlib.goferWeb as gw
from selenium.webdriver.chrome.options import Options
from pywinauto.keyboard import SendKeys

url=r'https://www.google.com/'
url='https://www.intel.com'
#driver = gw.init_chrome_driver()
co=Options()
#co.set_headless(headless=True)
# co.add_argument("--headless")
driver = webdriver.Chrome(executable_path=os.getcwd() + r'/goferlib/chromedriver', chrome_options=co)
driver.wait = WebDriverWait(driver, 5)
driver.get(url)

elem=driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//a[@class='btn btn-primary intel-cta']")))
print('element located!')
elem.click()
e=driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//a[contains(@class,'blade-item-link') and contains(@href, 'architecture')]")))

print(e.get_attribute('text'))
SendKeys('^s')
time.sleep(3)
SendKeys('test2{ENTER}')
time.sleep(10)
driver.quit()
