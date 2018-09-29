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
import time, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import goferlib.goferWeb as gw
url='http://www.mwave.me/en/signin'
url='http://www.google.com'
url=r'home/john/PycharmProjects/amc/home/john/PycharmProjects/amc/Art of Problem Solving.html'
url="file:///home/john/PycharmProjects/amc/Art%20of%20Problem%20Solving.html"
url='file:///'+os.getcwd()+r"\amc\Art%20of%20Problem%20Solving.html"
print(url)

driver = gw.init_chrome_driver()
driver.get(url)

driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//div[@id='mw-content-text']")))
# xpath search with multiple conditions, can be 'and', 'or'
# use * to replace 'a' if want to search any element with certain text
elem=driver.find_elements_by_xpath("//div[@id='mw-content-text']//ul//a[contains(text(), '19') or contains(text(), '20')]")
# //input[@name="username"] | //input[@id="wm_login-username"]

for i in elem:
    #i.click()
    print(i.get_attribute('href'))
print('path='+os.getcwd())
driver = gw.init_chrome_driver()
#driver=
driver.get(url)
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//span[@class='tit' and text()='google']")))
elem.click()

elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//input[@type='email']")))

#elem.send_keys(loginEmail)
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//span[@class='RveJvd snByac']")))
elem.click()
time.sleep(2) # will have error if not waiting the input page to appear
elem =driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//input[@type='password']")))

#elem.send_keys(loginPW)

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
"""
# If the element has two xpath, then you can write two xpaths like below
# xpath1 | xpath2
# Eg: //input[@name="username"] | //input[@id="wm_login-username"]
# //*[contains('abc') or contains('def') or text()='abcdef']
https://stackoverflow.com/questions/12562597/two-conditions-using-or-in-xpath
Two conditions using OR in XPATH

and and or are allowed inside the condition: [here]. Or you may also use multiple paths in one XPath expression using the pipe sign.

//PeopleList/Row[c1] | //PeopleList/Row[c2]


you can use or / and inside [....]

Example:

//*[contains('abc') or contains('def') or text()='abcdef']

More info about operators: http://www.w3schools.com/xpath/xpath_operators.asp

https://sqa.stackexchange.com/questions/10342/how-to-find-element-using-contains-in-xpath
I often use "contains", but there are more. Here are some examples:

    multiple condition: //div[@class='bubble-title' and contains(text(), 'Cover')]
    partial match: //span[contains(text(), 'Assign Rate')]
    starts-with: //input[starts-with(@id,'reportcombo')
    value has spaces: //div[./div/div[normalize-space(.)='More Actions...']]
    sibling: //td[.='LoadType']/following-sibling::td[1]/select"
    more complex: //td[contains(normalize-space(@class), 'actualcell sajcell-row-lines saj-special x-grid-row-collapsed')]

Take a look at the W3C XSL Functions page for some more ideas.

https://sqa.stackexchange.com/questions/10342/how-to-find-element-using-contains-in-xpath

By.xpath("//td[contains(text(),'youruser')]") //here user text is case sensitive

By.xpath("//td[contains(lower-case(text()),'youruser')]") //to handle case sensitivity. Here user is not case sensitive


.//*[@id='contentText']/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[10]/td/table/tbody/tr/td[1]/strong[2]

That XPath should be drastically shortened. That is likely to fail if you are testing in different browsers and if anything ever changes on the page it could throw a false positive due to it looking at the wrong element. I recommend looking up "Relative XPaths" and also "XPath Axes", but I could demonstrate a better XPath for you if you posted a screenshot of the HTML and the web page.

Based on what you posted, you could do something like: //table[@id ='something' or @class='Something that identifies this specific table']//tr[contains(text(), 'something to identify the row') or ./text() = 'Exact Text Match']//strong[2]

Usually with table rows I end up identifying the row based on the text from a cell within the row. //table[@id ='something' or @class='Something that identifies this specific table']//tr[.//td[contains(text(), 'something to identify the row') or ./text() = 'Exact Text Match']]//td//strong[2][contains(text(), 'Partial Text Match') or ./text() = 'Exact Text Match']


"//*[starts-with(@id, 'frag-') and contains(@id, '-0')]"

"""