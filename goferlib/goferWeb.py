from bs4 import BeautifulSoup
from bs4 import re
from urllib.request import urlopen
import selenium as sn
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time, os

def init_firefox_driver():
    print(os.getcwd() + "\n")
    driver = webdriver.Firefox(executable_path=r'C:\Users\qiangli3\PycharmProjects\jpy_2017\goferlib\geckodriver.exe')
    driver = webdriver.Firefox(executable_path=os.getcwd()+r'\geckodriver.exe')
    #driver = webdriver.Firefox()
    #os.System.setProperty("webdriver.gecko.driver", r'C:\Users\qiangli3\PycharmProjects\jpy_2017\goferlib\geckodriver.exe');
    driver.wait = WebDriverWait(driver, 5)
    #driver=webdriver()
    return driver
def init_chrome_driver():
    print('Chrome'+'path='+os.getcwd())
    driver = webdriver.Chrome(executable_path=os.getcwd() + r'\goferlib\chromedriver.exe')

    driver.wait = WebDriverWait(driver, 5)
    return driver

def get_soup_url(url):
    # init a selenium driver & get url's html
    # start a Firefox driver
    # driver = init_firefox_driver()
    # driver.get(url)
    # get html from driver
    html = urlopen(url)
    # driver.quit()  # remove this line to leave the browser open
    # print(html)   #test only
    # pass driver to bs
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_html_url(url):

    html = urlopen(url)
    # driver.quit()  # remove this line to leave the browser open

    return html

def get_soup_ff(url, ffDriver):
    # global ffDriver
    ffDriver.get(url)
    html = ffDriver.page_source
    ffDriver.wait = WebDriverWait(ffDriver, 5)
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_html(url, driver):
    # global ffDriver
    driver.get(url)
    html = driver.page_source
    driver.wait = WebDriverWait(driver, 5)
    return html
def chrome_test():
    driver = init_chrome_driver()
    html = get_html('http://www.google.com', driver)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()
def html_example():
    pass

