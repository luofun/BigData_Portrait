
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome=webdriver.Chrome()
url='http://www.phei.com.cn/'
chrome.get('http://www.phei.com.cn/')
'''assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)'''
time.sleep(10)
with open('phei.html','w',encoding='utf8') as f:
    f.write(chrome.page_source)
chrome.quit()
