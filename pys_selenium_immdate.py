"""
find N-400 processing date for Phoenix office
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
url='https://egov.uscis.gov/cris/processTimesDisplayInit.do'
driver = gw.init_chrome_driver()
driver.get(url)
#elem = driver.find_element_by_name("officeID")
elem = driver.wait.until(EC.presence_of_element_located(
        (By.ID, "officeSelect")))
#elem =driver.wait.until(EC.presence_of_element_located(
#                                  (By.CLASS_NAME, "gb_wb gb_Fa gb_7c gb_6c")))
print(elem.tag_name)
print(elem.get_property('attributes')[0])
print(elem.get_attribute('value'))
driver.execute_script("arguments[0].value='301'", elem)
elem=driver.wait.until(EC.presence_of_element_located(
        (By.NAME, "displayLOProcTimes")))

print(elem.tag_name)
elem.click()
# driver.find_elements_by_xpath("//*[contains(text(), 'N-400')]")
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//*[contains(text(), 'Application for Naturalization')]/following-sibling::td" )))
print(elem.tag_name)
procTime=driver.execute_script("return arguments[0].innerText;", elem)
print("proc time is :"+procTime)



import smtplib

TO = 'qiangli66@gmail.com'
SUBJECT = 'N-400 Phoenix Office processing time'
TEXT = procTime

# Gmail Sign In
"""
Must do: Allowing less secure apps to access your account
link:
https://myaccount.google.com/lesssecureapps

"""
gmail_sender = 'qiangli66@gmail.com'
gmail_passwd = 'Lq-516878'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
driver.close()