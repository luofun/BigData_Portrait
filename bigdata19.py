
import requests
url='https://www.jd.com/'
resp=requests.get(url)
s=resp.text
print(len(s))
with open('requests_jd.html','w',encoding='UTF-8') as f:
    f.write(s)
