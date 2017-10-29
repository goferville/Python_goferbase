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
from selenium.webdriver.common.action_chains import ActionChains
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
time.sleep(2)


#after lohin

elemName =driver.wait.until(EC.presence_of_element_located(
                                  (By.LINK_TEXT, 'Wanna One')))
print(elemName.get_attribute('innerHTML'))

elemName=elemName.find_element_by_xpath('../../..') #up one level
#hover mouse over theelement
hov = ActionChains(driver).move_to_element(elemName)
hov.perform()
time.sleep(2)
#end hover

#search page for appeared 'VOTE" button
#first search song name, then go up two directory for the button sectio
#find button and click
elemName =driver.wait.until(EC.presence_of_element_located(
                                  (By.LINK_TEXT, 'Wanna One')))
print(elemName.get_attribute('innerHTML'))
elemName=elemName.find_element_by_xpath('../../..') #up one level
print(elemName.get_attribute('innerHTML'))
elem=elemName.find_element_by_xpath(".//div[@class='info_box01']")
print(elem.get_attribute('innerHTML'))
elem.click()

elem =driver.wait.until(EC.presence_of_element_located(
                                 (By.XPATH, "//a[@id='select']")))
elem.click()