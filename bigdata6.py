import urllib
from urllib import request
from bs4 import BeautifulSoup
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url="http://www.cnblogs.com/jixin/p/5131040.html"
request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
soup=BeautifulSoup(response,'lxml')
a_lst=soup.find_all('a')
for a in a_lst:
    if a.text!="":
        print(a.text.strip(),a['href'])


