import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, csv

driver=webdriver.Firefox(executable_path=
                           r'C:\Users\gofer\PycharmProjects\Python_goferbase\geckodriver.exe')
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
#Press "more filters"button
extXpath="//div[@class='filters-overflow-button']"
eExt=driver.wait.until(EC.presence_of_element_located((By.XPATH,extXpath)))
eExt.click()
#-----------------------------
#color
#color :find element with style contains text 'left:28.571' - it's last digit changes everytime
clrXpath="//*[contains(@style,'left:28.571')]"
eClr=driver.wait.until(EC.presence_of_element_located((By.XPATH,clrXpath)))
eClr.click()
clrXpath="//*[contains(@class,'color-filter')]//div[@class='right handle']"

eClrMx=driver.find_element_by_xpath(clrXpath)
driver.execute_script("arguments[0].style = 'left: 57.1429%;'", eClrMx)
eClrMx.click()

#-----------------------------
#price
ePMaxpath="//*[contains(@class,'price-filter')]//input[@name='maxValue']"
ePMax=driver.find_element_by_xpath(ePMaxpath)
ePMax.send_keys("10000")
ePMax.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)
#-----------------------------
#carat
eCMinpath="//*[contains(@class,'carat-filter')]//input[@name='minValue']"
eCMin=driver.find_element_by_xpath(eCMinpath)
eCMin.send_keys("1.00")
eCMin.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)
eCMaxpath="//*[contains(@class,'carat-filter')]//input[@name='maxValue']"
eCMax=driver.find_element_by_xpath(eCMaxpath)
eCMax.send_keys("2.00")
eCMax.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)
#-----------------------------
#cut
eCutMinpath="//*[contains(@class,'cut-filter')]//div[@class='left handle min']"
eCutMin=driver.find_element_by_xpath(eCutMinpath)
driver.execute_script("arguments[0].style = 'right: 50%';", eCutMin)
eCutMin.click()
driver.implicitly_wait(0.3)
eCutMaxpath="//*[contains(@class,'cut-filter')]//div[@class='right handle']"
eCutMax=driver.find_element_by_xpath(eCutMaxpath)
driver.execute_script("arguments[0].style = 'left: 75%';", eCutMax)
eCutMax.click()
driver.implicitly_wait(0.3)
#-----------------------------
#clarity
eClaMinpath="//*[contains(@class,'clarity-filter')]//div[@class='left handle min']"
eClaMin=driver.find_element_by_xpath(eClaMinpath)
driver.execute_script("arguments[0].style = 'right: 75%';", eClaMin)
eClaMin.click()
driver.implicitly_wait(0.3)
eClaMaxpath="//*[contains(@class,'clarity-filter')]//div[@class='right handle']"
eClaMax=driver.find_element_by_xpath(eClaMaxpath)
driver.execute_script("arguments[0].style = 'left: 37.5%';", eClaMax)
eClaMax.click()
driver.implicitly_wait(0.3)
#-----------------------------
#polish
#toggle on
ePolpath="//*[contains(@class,'polish-filter')]//div[@class='toggle-button-switch']"
#ePol=driver.wait.until(EC.presence_of_element_located((By.XPATH,ePolpath)))
ePol=driver.find_element_by_xpath(ePolpath)
ePol.click()
driver.implicitly_wait(0.5)
#set max min - only min
ePolMinpath="//*[contains(@class,'polish-filter')]//div[@class='left handle min']"

ePolMin=driver.find_element_by_xpath(ePolMinpath)
driver.execute_script("arguments[0].style = 'right: 33.3333%;'", ePolMin)
ePolMin.click()
driver.implicitly_wait(0.3)

#ePolMaxpath="//*[contains(@class,'polish-filter')]//div[@class='right handle']"
#ePolMax=driver.find_element_by_xpath(ePolMaxpath)
#driver.execute_script("arguments[0].style = 'left: 37.5%';", ePolMax)
#ePolMax.click()
#driver.implicitly_wait(0.3)

#-----------------------------
#symmetry
#toggle on
eSympath="//*[contains(@class,'symmetry-filter')]//div[@class='toggle-button']"
#eSym=driver.wait.until(EC.presence_of_element_located((By.XPATH,eSympath)))
eSym=driver.find_element_by_xpath(eSympath)
eSym.click()
driver.implicitly_wait(0.5)
#set max min - only min
eSymMinpath="//*[contains(@class,'symmetry-filter')]//div[@class='left handle min']"
eSymMin=driver.find_element_by_xpath(eSymMinpath)
driver.execute_script("arguments[0].style = 'right: 33.3333%;'", eSymMin)
eSymMin.click()
driver.implicitly_wait(0.3)
#-----------------------------
#fluorescence
#toggle on
eFlopath="//*[contains(@class,'fluorescence-filter')]//div[@class='toggle-button']"
#eSym=driver.wait.until(EC.presence_of_element_located((By.XPATH,eSympath)))
eFlo=driver.find_element_by_xpath(eFlopath)
eFlo.click()
#-----------------------------
#depth
#toggle on
eDeppath="//*[contains(@class,'depth-filter')]//div[@class='toggle-button']"
#eDep=driver.wait.until(EC.presence_of_element_located((By.XPATH,eDeppath)))
eDep=driver.find_element_by_xpath(eDeppath)
eDep.click()
driver.implicitly_wait(0.5)
#set min max
eDMinpath="//*[contains(@class,'depth-filter')]//input[@name='minValue']"
eDMin=driver.find_element_by_xpath(eDMinpath)
eDMin.send_keys("60%")
eDMin.send_keys(Keys.RETURN)
driver.implicitly_wait(0.3)
eDMaxpath="//*[contains(@class,'depth-filter')]//input[@name='maxValue']"
eDMax=driver.find_element_by_xpath(eDMaxpath)
eDMax.send_keys("62%")
eDMax.send_keys(Keys.RETURN)
driver.implicitly_wait(0.3)

#-----------------------------
#Table
#toggle on
eDeppath="//*[contains(@class,'table-filter')]//div[@class='toggle-button']"
#eDep=driver.wait.until(EC.presence_of_element_located((By.XPATH,eDeppath)))
eDep=driver.find_element_by_xpath(eDeppath)
eDep.click()
driver.implicitly_wait(0.5)
#set min max
eDMinpath="//*[contains(@class,'table-filter')]//input[@name='minValue']"
eDMin=driver.find_element_by_xpath(eDMinpath)
eDMin.send_keys("55%")
eDMin.send_keys(Keys.RETURN)
driver.implicitly_wait(0.3)
eDMaxpath="//*[contains(@class,'table-filter')]//input[@name='maxValue']"
eDMax=driver.find_element_by_xpath(eDMaxpath)
eDMax.send_keys("58%")
eDMax.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)

#-----------------------------
#price-per-carat-filter
#toggle on
#ePpcpath="//*[contains(@class,'price-per-carat-filter')]//button[@class='column-toggle-filter']"
ePpcpath="//*[contains(@class,'price-per-carat-filter')]//div[@class='filter-content add-column']"
#ePpcpath="//*[contains(@class,'price-per-carat-filter')]//span[@class='small tooltip']"
#ePpc=driver.wait.until(EC.presence_of_element_located((By.XPATH,ePpcpath)))
ePpc=driver.find_element_by_xpath(ePpcpath)
ePpc.click()

driver.implicitly_wait(0.5)
#somehow need click twice to active
ePpc.click()
driver.implicitly_wait(0.5)
#-----------------------------
#culet
#toggle on
#eCltpath="//*[contains(@class,'culet-filter')]//button[@class='column-toggle-filter']"
eCltpath="//*[contains(@class,'culet-filter')]//div[@class='filter-content add-column']"
#eClt=driver.wait.until(EC.presence_of_element_located((By.XPATH,eCltpath)))
eClt=driver.find_element_by_xpath(eCltpath)
eClt.click()
driver.implicitly_wait(0.5)
#-----------------------------
#price-per-carat-filter
#toggle on
time.sleep(2)
xPath="//button[contains(@class,'tab selected')]/span"
elem=driver.find_element_by_xpath(xPath)
ttext=str(elem.get_attribute('innerHTML'))
print(ttext)
sind=ttext.find('(<!-- -->')+9
eind=ttext.find('<!-- -->)')
print(sind,eind,ttext[sind:eind])
xPath="//a[contains(@href,'./diamond-details/LD')]"
rows=driver.find_elements_by_xpath(xPath)
print(len(rows))
dl=[]
#dl.append(['inde','BL id','price'])
i=1
for row in rows:
    href=row.get_attribute('href')
    st=href.find("ils/LD")
    se=href.find("?ref")
    bnid=href[st+4:se]
    #print(row.get_attribute('href'))
    subXpath=".//div[contains(@class,'row-cell price')]/span"
    pricecell=row.find_element_by_xpath(subXpath).text
    bnprice=(pricecell[1:]).replace(",","")
    print("ID=",bnid,"   price=",bnprice)
    dl.append([str(i),bnid,bnprice])
    i+=1
with open('di_list_2018.csv','w', newline='') as f:
    writer=csv.writer(f)
    for row in dl:
        writer.writerow(row)


