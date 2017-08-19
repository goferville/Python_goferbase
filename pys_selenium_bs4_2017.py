from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_firefox_driver():
    driver = webdriver.Firefox(executable_path=r'C:\Users\koala\PycharmProjects\Python_goferbase\geckodriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def get_soup_obj(url):
    # init a selenium driver & get url's html
    # start a Firefox driver
    driver = init_firefox_driver()
    driver.get(url)
    # get html from driver
    html = driver.page_source
    # driver.quit()  # remove this line to leave the browser open
    # print(html)   #test only
    # pass driver to bs
    soup = BeautifulSoup(html, "html.parser")
    return soup


def soup_test(soup):
    for link in soup.find_all('a'):
        print(link.get('href', None))


def basic_test():
    url = 'http://www.google.com'
    soup = get_soup_obj(url)
    # further parsing: do something with bs object
    soup_test(soup)


def text_parse_test():
    print("1. === basic scrapping ===")
    # Book "web scraping with Python", P. 14
    url = 'http://www.pythonscraping.com/pages/warandpeace.html'
    soup = get_soup_obj(url)
    #nameList = soup.find_all("span",{"class":"green"})
    #for name in nameList:
    #    print(name.get_text())
    # following should return both red and green tag, but only last was returned
    # cannot be use dlike this according to bs4 document
    combinedList = soup.find_all("span", {"class": "green", "class": "red"})
    for cName in combinedList:
        print(cName.get_text())
    # Qs???: problem with "the Prince"
    # also see how I convert integer to string
    pList = soup.find_all(text="the prince")
    print("the Prince ="+len(pList).__str__())


    # test .children
    print("2. === test .children ===")
    url = 'http://www.pythonscraping.com/pages/page3.html'
    soup = get_soup_obj(url)
    for child in soup.find("table", {"id": "giftList"}).children:
        print(child)



text_parse_test()
