import urllib
from urllib import request
from bs4 import BeautifulSoup
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url="http://www.baidu.com"
request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
soup=BeautifulSoup(response)
print(soup)
data=soup.find_all("baidu")
print(data)