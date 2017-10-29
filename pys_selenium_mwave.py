"""
MWave operation
"""
from bs4 import BeautifulSoup
from bs4 import re
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import goferlib.goferWeb as gw
url='http://www.mwave.me/en/signin'
voteUrl='http://www.mwave.me/en/vote/mama/vote'
loginEmail='goferville@gmail.com'
loginPW='lb555555'
driver = gw.init_chrome_driver()
driver.get(url)
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//span[@class='tit' and text()='google']")))
elem.click()

elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//input[@type='email']")))

elem.send_keys(loginEmail)
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//span[@class='RveJvd snByac']")))
elem.click()
time.sleep(2) # will have error if not waiting the input page to appear
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//input[@type='password']")))

elem.send_keys(loginPW)

elem =driver.wait.until(EC.presence_of_element_located(
                                 (By.XPATH, "//span[@class='RveJvd snByac']")))
elem.click()
time.sleep(3)
driver.get(voteUrl)
time.sleep(3)
elemName =driver.wait.until(EC.presence_of_element_located(
                                 (By.XPATH, "//*[contains(text(),'Wanna One']")))
elemName=elemName.find_element_by_xpath('../../..') #up one level
print(elemName.get_attribute('innerHTML'))
#elem = elemName.find_element_by_xpath(".//*[contains(text(), 'VOTE')]")
#elem.click()