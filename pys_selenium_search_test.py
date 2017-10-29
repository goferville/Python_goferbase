from bs4 import re
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import goferlib.goferWeb as gw
url='http://site.6park.com/enter1/index.php?app=forum&act=list'

driver = gw.init_chrome_driver()
driver.get(url)
elemName =driver.wait.until(EC.presence_of_element_located(
                                  (By.LINK_TEXT, '醋一千怎么解，三国怎么解？ (无内容)')))

elemName=elemName.find_element_by_xpath('../../..') #up one level

#elemName =driver.wait.until(EC.presence_of_element_located(
                                 #(By.XPATH, "//span[@class='t_views_14233403']")))

#elemName=elemName.find_element_by_xpath('..') #up one level
print(elemName.get_attribute('innerHTML'))
elem = elemName.find_element_by_xpath("*[contains(text(), '一哥们')]")

print(elem.tag_name)
#elem = elemName.find_element_by_link_text('一哥们蚂蚁借呗借了八千多，然后把支付宝卸载了[笑话]')
elem.click()
#elemName.click()
'绿卡不再是护身符!美国今年入籍申请量大增(图)'
