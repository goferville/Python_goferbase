import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path=
                           r'C:\Users\qiangli3\Documents\Python\PyCharmProj\venv1\geckodriver.exe')
driver.wait = WebDriverWait(driver, 5)
#load a local html filr url="file://"+filepath+filename
#url_inhouse=r"file://C:\Users\qiangli3\Documents\Python\PyCharmProj\html_test_3.html"
#driver.get(url_inhouse)
url_bn="https://www.bluenile.com/diamond-search?track=NavDiaSeaRD"
driver.get(url_bn)
# driver.implicitly_wait(5)
#elem = driver.wait.until(EC.presence_of_element_located((By.ID,"t01")))
colorH="left:28.57142857142857%;"
colorSel=colorH
extcolorSel="//div[@style='"+colorSel+"']"
print(colorSel)
#elem = driver.wait.until(EC.presence_of_element_located((By.XPATH,colorSel)))
extXpath="//span[@class='extra']"
driver.wait.until(EC.presence_of_element_located((By.XPATH,extXpath)))
#color :find element with style contains text 'left:28.571' - it's last digit changes everytime
elem=driver.find_element_by_xpath("//*[contains(@style,'left:28.571')]")
print(elem.get_attribute("style"))
elem.click()
ePMax=driver.find_element_by_xpath("//input[@name='maxValue'][@value='$3,643,049']")
ePMax.send_keys("10000")
ePMax.send_keys(Keys.RETURN)
driver.implicitly_wait(1)
eCMin=driver.find_element_by_xpath("//input[@name='minValue'][@value='0.23']")
eCMin.send_keys("1.00")
eCMin.send_keys(Keys.RETURN)
driver.implicitly_wait(1)
eCMax=driver.find_element_by_xpath("//input[@name='maxValue'][@value='20.05']")
eCMax.send_keys("2.00")
eCMax.send_keys(Keys.RETURN)
driver.implicitly_wait(1)
#Cut: click on 50% then 75% to make sure left handle moves
#first selected 50% is clarity
eCut=driver.find_element_by_xpath("//div[@class='option-mark'][@style='left:25%;']")
eCut.click()
driver.implicitly_wait(0.5)
eCut=driver.find_element_by_xpath("//div[@class='left handle '][@style='right: 75%;']")
#move left handle to right 75% then click to set value
driver.execute_script("arguments[0].style = 'right: 25%';", eCut)
eCut.click()
#Select Cla -- Clarity, click on left level first, so next click will still ne left handle
eCla=driver.find_element_by_xpath("//div[@class='option-mark'][@style='left:12.5%;']")
eCla.click()
driver.implicitly_wait(0.5)
#find 'left:37.5%;' then find next 'left:50%;' by using nextsibling or 'left:37.5%;' is not unique
eCla=driver.find_element_by_xpath("//div[@class='option-mark'][@style='left:37.5%;']/following-sibling::div")
eCla.click()
"""
elem = driver.wait.until(EC.presence_of_element_located((By.XPATH,"//h2[@id='id1']")))
print(elem.get_attribute('text'),elem.get_attribute('innerHTML'))
elems=driver.find_elements_by_xpath("//h2")
for e in elems:
    print(e.get_attribute("innerHTML"))
"""
#here attribute of a HTML element
#driver.find_element_by_xpath( "//div[@data-user-id='30646' or @data-shift-date='2016-10-15']").click()
