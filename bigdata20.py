from selenium import webdriver
import time
def scroll(n,i):
    return "window.scrollTo(0,(document.body.scrollHeight/{0})*{1});".format(n,i)

url='https://www.jd.com/'
chrome=webdriver.Chrome()
chrome.maximize_window()
chrome.get(url)

n=10
for i in range(1,n+1):
    s=scroll(n,i)
    print(s)
    chrome.execute_script(s)
    time.sleep(2)

print(len(chrome.page_source))
with open('selenium_jd.html','w',encoding='UTF-8',errors='ignore') as f:
    f.write(chrome.page_source)

