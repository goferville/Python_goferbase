import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, csv

def dbyid(driver,id):
    try:
        e = driver.find_element_by_id(id)
        data = str(e.get_attribute('innerHTML'))
        print(id, " = ", data)
    except:
        data="no data"

    return data

ps=["REPORT_NO","REPORT_DT","LENGTH","WEIGHT","COLOR","CLARITY","FINAL_CUT","DEPTH_PCT",
    "TABLE_PCT","CRN_AG","CRN_HT","PAV_AG","PAV_DP","STR_LN","LR_HALF","GIRDLE",
    "CULET_SIZE","POLISH","SYMMETRY","FLUORESCENCE_INTENSITY","KEY_TO_SYMBOLS"]
csvTitle=['index','BN id','price','GIA id','BN id2']
for p in ps:
    csvTitle.append(p)
giaData=[]
#prepare web driver
driver=webdriver.Firefox(executable_path=
                           r'C:\Users\gofer\PycharmProjects\Python_goferbase\geckodriver.exe')
driver.wait = WebDriverWait(driver, 5)
#load a local html filr url="file://"+filepath+filename
#url_inhouse=r"file://C:\Users\qiangli3\Documents\Python\PyCharmProj\html_test_3.html"
#driver.get(url_inhouse)
url_gia="https://www.gia.edu/"
driver.get(url_gia)
eid="search-value"
e=driver.wait.until(EC.presence_of_element_located((By.ID,eid)))
eSpath="//input[@id='search-value']"
e=driver.wait.until(EC.presence_of_element_located((By.XPATH,eSpath)))



with open('bn_gia_list_2018.csv','r') as fr:
    csvReader = csv.reader(fr)
    i=1
    for row in csvReader:
        i=int(row[0])
        print(i)
        if i>49:
            #
            gia=row[3]
            e = driver.wait.until(EC.presence_of_element_located((By.XPATH, eSpath)))
            e.send_keys(gia)
            e.send_keys(Keys.RETURN)
            driver.implicitly_wait(0.3)
            time.sleep(5)#
            gNo="Loading"
            ldI=0
            while gNo=="Loading":
                ids=ps[0]
                gNo = dbyid(driver, ids)
                time.sleep(1)
                ldI +=1
                if ldI>5:
                    try:
                        e = driver.find_element_by_id("recaptcha_response_field")
                        e.send_keys("v1 shutdown on 2018-03-31")
                        e.send_keys(Keys.RETURN)
                        driver.implicitly_wait(5)
                    except:
                        print("No capt found error!")


            for p in ps:
                row.append(dbyid(driver,p))
            #giaData.append(row)
            print(row)
            with open('di_giadata_2018.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)
"""            
           # with open('di_giadata_2018.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(csvTitle)
                for row in giaData:
                    writer.writerow(row)

"""

