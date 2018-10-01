"""
AMC
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
import time, os, csv
from pywinauto.keyboard import SendKeys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import goferlib.goferWeb as gw

def saveamc(fname):
    amcPath = r'C:\Users\gofer\PycharmProjects\Python_goferbase' + '\\'

    fn=amcPath+fname+'.html'+'{ENTER}'

    SendKeys('^s')
    time.sleep(2)
    SendKeys(fn)
    time.sleep(3)
# var to hold q set name and set year
amc_year=[]
nRow=0 #index of total row in csv file


amcFileName='amc.csv'
amcData=[['questionSetTitle','questionSetYear','questionSetType', 'questionSetURL', 'questionTitle', 'questionNumber', 'questionURL',
          'questionAnswerKey','questionSol1URL']]

# amcDataTmp is the place holder at the beginning of each data filling, len=9

# new test year start row



url='https://artofproblemsolving.com/wiki/index.php?title=AMC_8_Problems_and_Solutions'
#url=r'home/john/PycharmProjects/amc/home/john/PycharmProjects/amc/Art of Problem Solving.html'
#url=r"file:///home/john/PycharmProjects/amc/Art%20of%20Problem%20Solving.html"
#url=r'file:///'+os.getcwd()+r"\amc\Art%20of%20Problem%20Solving.html"
print(url)

driver = gw.init_chrome_driver()
driver.get(url)

driver.wait.until(EC.presence_of_element_located(
                                  (By.XPATH, "//div[@id='mw-content-text']")))
# xpath search with multiple conditions, can be 'and', 'or'
# use * to replace 'a' if want to search any element with certain text
elem=driver.find_elements_by_xpath("//div[@id='mw-content-text']/ul//a[contains(text(), '19') or contains(text(), '20')]")
# //input[@name="username"] | //input[@id="wm_login-username"]

# acquire all year title and link -> amc_year
for i in elem:
    amc_year.append([i.get_attribute('text'),i.get_attribute('href')])
    questionSetTitle=i.get_attribute('text')
    questionSetURL=i.get_attribute('href')


cn=1
# get data for each year
for ay in amc_year:
    if cn>25:
        # tmp for P, PAKey,P&S links,
        tmpPUrl = []  # 0: Problems url; 1: Answer Key url

        tmpPName = []  # Problem name
        tmpAN = []  # for each answer key under tmpAKUrl

        tmpPNUrl = []  # for each problem url
        tmpSNUrl = []  # for each solution url
        # ------------------
        # Title, year, set name, set url for current year ay
        aTitle = ay[0]
        aYear = (ay[0].split(' '))[0]
        aSetType = (ay[0].split(' '))[1]
        aSetUrl = ay[1]
        print('year=', aYear, 'SetTitle=', aTitle, 'url=', aSetUrl, 'Type=', aSetType)
        # ------------------

        # Open question page of current year
        driver.get(aSetUrl)
        # driver.get(r'https://artofproblemsolving.com/wiki/index.php?title=2002_AMC_8')
        # driver.get(r'https://artofproblemsolving.com/wiki/index.php?title=2003_AMC_8')
        # driver.get(r'https://artofproblemsolving.com/wiki/index.php?title=1998_AJHSME')
        driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='mw-content-text']")))
        fn = aTitle.replace(' ', '_')
        fp = 'amc' + '\\' + fn
        os.makedirs(fp)
        fname = fp + '\\' + fn
        # print(fname)
        saveamc(fname)
        ayElemL1 = driver.find_elements_by_xpath(
            "//div[@id='mw-content-text']/ul/li/a[contains(@href, 'Problems') or contains(@href, 'Answer')]")
        ayElemL2 = driver.find_elements_by_xpath(
            "//div[@id='mw-content-text']/ul/li/ul/li/a[contains(text(), 'Problems')]")

        for e in ayElemL1:
            tmpPUrl.append(e.get_attribute('href'))
            print("tmpUrl=", tmpPUrl)
        # count n of problems, fill solution url array
        nProblems = 0;
        for e in ayElemL2:
            tmpSNUrl.append(e.get_attribute('href'))
            tmpPName.append(e.get_attribute('text'))
            nProblems += 1
        probListUrl = ''
        print("PN URL=", tmpPUrl[0], tmpPUrl[1])
        driver.get(tmpPUrl[0])  # problem list link
        driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//li[contains(@class, 'toclevel-')]")))
        saveamc(fname + '_ProblemList')
        tmpPNUrl_elem1 = driver.find_elements_by_xpath("//li[contains(@class, 'toclevel-')]//a[contains("
                                                       "@href, "
                                                       "'Problem')]")
        for e in tmpPNUrl_elem1:
            tmpPNUrl.append(e.get_attribute('href'))
        driver.get(tmpPUrl[1])  # answer key list link
        driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='mw-content-text' and @class='mw-content-ltr']")))
        saveamc(fname + '_AnswerKey')
        tmpPNUrl_elem2 = driver.find_elements_by_xpath("//div[@id='mw-content-text' and @class='mw-content-ltr']/ol/li")
        for e in tmpPNUrl_elem2:
            tmpAN.append(e.get_attribute('innerHTML'))
        print('Len AN=', len(tmpAN), 'Len PN=', len(tmpPNUrl))
        for i in range(nProblems):
            amcData.append([aTitle, aYear, aSetType, aSetUrl, tmpPName[i], i + 1, tmpPNUrl[i], tmpAN[i], tmpSNUrl[i]])
        for i in range(nProblems):
            driver.get(tmpSNUrl[i])
            driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//span[contains(@id, 'Solution')]")))
            saveamc(fname + '_Solution_' + str(i + 1))
        print("n Q=", nProblems)
        print('problem list', tmpPNUrl)
        print('answerkey', tmpAN)
        print('solution list', tmpSNUrl)

        # break;
    cn=cn+1
#setup csv file
fw=open('amc.csv','w', newline='')
cw = csv.writer(fw)
for ad in amcData:
    cw.writerow(ad)
fw.close()

#print(amc_year, "Problems=", nProblems)
driver.close()
driver.quit()
'data = questionsID, questionSetTitle, questionSetURL questionTitle questionNumber questionURL questionAnswerKey ' \
'questionSol1 questionSol1URL questionSetYear'
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
