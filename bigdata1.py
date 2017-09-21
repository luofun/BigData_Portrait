#coding=utf-8 

import requests
import io
import sys
#import BeautifulSoup
from pyquery import PyQuery as pq 

def get_content(url):
    resp =requests.get(url)
    return resp.text

url="https://www.baidu.com"

content=get_content(url)

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')   

#content2 = str(content,'utf-8')

#print("500charaters: ",content[0:500])

print("我是汉字")

html =str(content)


'''r = requests.get('http://www.baidu.com') 
r.text 
type(r.text) 
html2 = pq(r.text) 
print( html2('title').text()) 
'''
#test1=beautifulSoup4(html)

#print(test1)

#str = unicode(html, 'gbk') 

html=html.encode('utf-8')



print(html)

content_len =len(content)

print("length: ",content_len)


f = open("out.html","w",encoding='utf-8')  

f.write(str(html))  



"""lst='\xe4\xb8\xad\xe5\x9b\xbd\xe6\x89\x8b\xe6\xb8\xb8\xe6\x9f\x90\xe7\xab\x99\xe5\xa4\xa7\xe9\x87\x8f\xe5\xbc\xb1\xe5\x8f\xa3\xe4\xbb\xa4\xe6\xb3\x84\xe9\x9c\xb2\xe5\xa4\xa7\xe9\x87\x8f\xe5\x91\x98\xe5\xb7\xa5\xe4\xb8\xaa\xe4\xba\xba\xe4\xbf\xa1\xe6\x81\xaf/\xe5\xb7\xa5\xe8\xb5\x84/\xe5\x86\x85\xe9\x83\xa8\xe6\x9e\xb6\xe6\x9e\x84\xe7\xad\x89'

#print(str(lst).decode('string_escape'))
for a in lst:
  print(a)
"""


if content_len >= 40*1024:
    print("bigger than 40KB")
else:
    print("smaller than 40KB")